#! /usr/bin/env python3

#modules for ros
import rospy
import rospkg
from sensor_msgs.msg import Image
import message_filters
from cv_bridge import CvBridge, CvBridgeError

#modules for mmdetection
from mmdet.apis import inference_detector, init_detector,show_result_pyplot
import mmcv

#modules for tracking
from sort import *

#modules for self-defined message
from swin_detection.msg import Object

#modules for annotation
from image_info import *

#general modules
from datetime import datetime
import json
import os
import cv2
import numpy as np
import shutil


image_table=ImageTable()

class Detection:
    def __init__(self,config_file,checkpoint_file):

        #load the config file and checkpoint for neural network trained by mmdetection
        self.config=config_file
        self.checkpoint=checkpoint_file

        #class_name for classification
        self.class_names=['Can', 'Carton/Paper', 'GlassBottle',
         'Other', 'PlasticBottle', 'PlasticOther', 'Wrapper']

        # convert ros message to opencv data
        self.bridge=CvBridge()

        # load mmdetection detector
        self.load_detector()

        # load tracker for objects
        self.setupTracker()

        # initialize the annotation id for objects
        self.annotation_id=1

        #subscribe rgb_image topic and depth_image topic
        self.sub_rgb=message_filters.Subscriber("/camera/color/image_raw",Image,)
        self.sub_depth=message_filters.Subscriber("/camera/aligned_depth_to_color/image_raw",Image)

        #synchronize two topic and trigger callback function
        ts=message_filters.TimeSynchronizer([self.sub_rgb,self.sub_depth],10000)
        ts.registerCallback(self.processImages)


    def load_detector(self,device='cuda:0'):
        self.detector = init_detector(config_file, checkpoint_file, device=device)

    # core function to process images
    def processImages(self, color_img_msg,depth_img_msg,):

        # convert ros message to opencv type
        cv_img = self.bridge.imgmsg_to_cv2(color_img_msg, desired_encoding="bgr8")
        depth_img=self.bridge.imgmsg_to_cv2(depth_img_msg, desired_encoding="passthrough")

        # normalize depth information to show
        depth_img_new=depth_img/depth_img.max()*255
        depth_img_new=depth_img_new.astype(np.uint8)

        # flag to trigger detection
        flag=depth_img[np.where(np.logical_and(depth_img>10,depth_img<810))]#and np.where(depth_img>10)

        #initialize return result to prevent blank images
        contour_img = 255 * np.ones(cv_img.shape, dtype=np.uint8)
        track_img=np.copy(cv_img)
        cv_img_new=np.copy(cv_img)

        # if flag.shape[0]>0:

        # get the bbox and segmentation result for current image.
        bbox_result, segm_result =inference_detector(self.detector,cv_img)

        # preprocess the bbox_result and segm_result
        bboxes,segms,labels,scores=self.preprocess(bbox_result,segm_result,cv_img,score_thr=0.9)

        # draw bbox ,segmentation mask, and contour
        cv_img_new,contour_img=self.draw_bbox_mask(bboxes,segms,labels,cv_img)

        # feed bboxes, get tracking result for object (correspondance:object_id--bbox_id)
        unique_detections = self.sort_tracker.update(bboxes)
        rospy.loginfo(unique_detections)
        correspondances = self.sort_tracker.detection_to_tracker

        # draw object_id
        track_img=self.draw_bbox_id(bboxes,cv_img,correspondances)

        #extract information
        self.extract_info(bboxes,segms,labels,correspondances,cv_img)

        #save annotations for retraining
        self.save_annotation(bboxes,segms,labels,correspondances,cv_img)

        # publish corresponding message to visualize
        self.pub_rgb=rospy.Publisher("/test_image",Image,queue_size=100)
        self.pub_depth=rospy.Publisher("/test_depth",Image,queue_size=100)
        self.pub_contour=rospy.Publisher("/test_contour",Image,queue_size=100)
        self.pub_track=rospy.Publisher("/test_track",Image,queue_size=100)


        image_message_rgb = self.bridge.cv2_to_imgmsg(cv_img_new,"bgr8")
        image_message_depth=self.bridge.cv2_to_imgmsg(depth_img_new,"mono8")
        image_message_contour=self.bridge.cv2_to_imgmsg(contour_img,"bgr8")
        image_message_track=self.bridge.cv2_to_imgmsg(track_img,"bgr8")

        self.pub_rgb.publish(image_message_rgb)
        self.pub_depth.publish(image_message_depth)
        self.pub_contour.publish(image_message_contour)
        self.pub_track.publish(image_message_track)

    #draw bbox,segmentation mask and contour
    def draw_bbox_mask(self,bboxes,segms,labels,img):
        """
        input:
        bboxes([[],[],...])
        segms(mask)
        labels([...])
        img:rgb_image

        output:
        new_img:images with mask and bboxes
        contour_img:images with contour

        """
        # initialize new_img and contour_image
        new_img=np.copy(img)
        contour_img=255*np.ones(img.shape,dtype=np.uint8)

        # draw segmentation mask
        for i,label in enumerate(labels):

            # color for the mask
            color_mask=np.array([100,100,0])

            # convert to boolean to fit in extract_boundary function
            mask=segms[i].astype(bool)
            new_img[mask]=new_img[mask]*0.5 + color_mask * 0.5
            contour,tmp=self.extract_boundary(mask)

            contour_img=cv2.drawContours(contour_img, contour, 0, (0, 0, 0), 2)

        # draw bounding box ,class name and score
        for i, (bbox, label) in enumerate(zip(bboxes, labels)):

            bbox_int = bbox.astype(np.int32)

            poly = [[bbox_int[0], bbox_int[1]], [bbox_int[0], bbox_int[3]],
                    [bbox_int[2], bbox_int[3]], [bbox_int[2], bbox_int[1]]]
            np_poly = np.array(poly).reshape((4, 2))
            new_img=cv2.rectangle(new_img,np_poly[0,:],np_poly[2,:],color=(0,0,255),thickness=2)

            label_text = self.class_names[label]
            label_text += f'|{bbox[-1]:.02f}'
            new_img=cv2.putText(new_img,label_text,(bbox_int[0],bbox_int[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),thickness=2)

        return new_img,contour_img

    # draw bounding box id (object_id)
    def draw_bbox_id(self,bboxes,cv_img,correspondances):
        """
        input:
        bboxes:[[],[]]
        cv_img:rgb_img
        correspondances:output by tracker

        output:
        new_img: images with tracking id
        """
        #initialize tracking image
        new_img = np.copy(cv_img)

        for i,bbox in enumerate(bboxes):
            if i>=len(correspondances):
                continue
            # draw bounding box
            bbox_int = bbox.astype(np.int32)
            poly = [[bbox_int[0], bbox_int[1]], [bbox_int[0], bbox_int[3]],
                    [bbox_int[2], bbox_int[3]], [bbox_int[2], bbox_int[1]]]
            np_poly = np.array(poly).reshape((4, 2))
            new_img = cv2.rectangle(new_img, np_poly[0, :], np_poly[2, :], color=(0, 0, 255),thickness=2)

            #draw tracking id
            id=f"{correspondances[i][1]+1}"
            new_img=cv2.putText(new_img,id,(bbox_int[0],bbox_int[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),thickness=2)

        return new_img

    # extract boundary based on opencv,tmp is for publishing ros message
    def extract_boundary(self,mask):
        mask=mask.astype(np.uint8)
        contour,_=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        tmp=np.array(contour[0])
        tmp=np.squeeze(tmp,axis=1)
        tmp=tmp.flatten()

        return contour,tmp

    #initialize tracker
    def setupTracker(self):
        """Setup the tracker using Simple Online Rapid Tracking"""

        # Max age, and min age are relevant parameters for avoiding duplicate tracking.
        self.sort_tracker = Sort(max_age=20, min_hits=20, iou_threshold=0.3)

    # preprocess output from mmdetection detector to facilitate visualization
    def preprocess(self,bbox_result,segm_result,img,score_thr):
        new_img = np.copy(img)

        bboxes = np.vstack(bbox_result)
        scores = bboxes[:, -1]
        labels = [
            np.full(bbox.shape[0], i, dtype=np.int32)
            for i, bbox in enumerate(bbox_result)
        ]
        labels = np.concatenate(labels)

        inds=scores>score_thr
        bboxes=bboxes[inds,:]
        labels=labels[inds]

        segms = []
        if len(labels>0):
            segms = mmcv.concat_list(segm_result)
            segms = np.stack(segms, axis=0)
            segms=segms[inds,...]

        return bboxes,segms,labels,scores

    # extract image information for publishing message to other nodes
    # refer to the msg/Object.msg
    def extract_info(self,bboxes,segms,labels,correspondances,img):

        # publish to the object_information_subsribe node
        self.pub_info=rospy.Publisher("/test_info",Object,queue_size=1000)

        for i, (bbox, label) in enumerate(zip(bboxes, labels)):
            if i>=len(correspondances):
                continue

            #bbox,mask,segmentation points for every bounding box
            bbox_int = bbox.astype(np.int32)
            mask=segms[i]
            _,segm_points=self.extract_boundary(mask)

            # initialize Object message
            msg=Object()

            # time for name
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
            msg.time=dt_string

            msg.place=rospy.get_param("location")

            msg.name=self.class_names[label]

            msg.category_id=label

            cropped_image=img[ bbox_int[1]:bbox_int[3],bbox_int[0]:bbox_int[2]]
            msg.cropped_image=self.bridge.cv2_to_imgmsg(cropped_image,"bgr8")

            msg.image_rgb=self.bridge.cv2_to_imgmsg(img,"bgr8")

            msg.id=correspondances[i][1]+1

            msg.bbox=bbox[0:4]

            msg.segm=segm_points

            msg.score=bbox[-1]

            self.pub_info.publish(msg)

    # save annotation for retraining
    def save_annotation(self,bboxes,segms,labels,correspondances,img):
        rospack = rospkg.RosPack()
        path = rospack.get_path("swin_detection")

        path = path + "/output_multi"
        if not os.path.exists(path):
            os.mkdir(path)
        output_file = path + "/annotations_multi.json"


        if not os.path.exists(output_file):
            with open(output_file, "w") as f:
                data = {}
                data["info"] = []
                data['images'] = []
                data['annotations'] = []
                data['categories'] = []

                data["licenses"] = []
                f.write(json.dumps(data))
            f.close()

        with open(output_file) as f:
            data=json.loads(f.read())


        image_info=ImageInfo(bboxes, segms, labels, correspondances, img)
        image_info.split()
        image_table.add(image_info)
        image_selected,current_object_id=image_table.select()

        if image_selected is not None:
            image_prefix=path+"/images/"
            if not os.path.exists(image_prefix):
                os.mkdir(image_prefix)

            # save image
            image_name = "frame" + f"{current_object_id}".zfill(6) + ".png"
            cv2.imwrite(image_prefix + image_name, image_selected.img)

            # write image information
            data["images"].append({"id": current_object_id, "width": img.shape[1], "height": img.shape[0],
                                   "file_name": "images/" + image_name})


            # categories information
            # object number in current frames
            for i in range(len(image_selected.object_info_list)):
                if not image_selected.labels[i] in [item["id"] for item in data["categories"]]:

                    data["categories"].append({"id": int(image_selected.labels[i]), "name": self.class_names[image_selected.labels[i]]})

            # "annotation part"
                item=image_selected.object_info_list[i]

                segment_info=item.segment_points.astype(np.float64)
                segment_info=list(segment_info)

                data["annotations"].append({
                        "id": int(self.annotation_id),
                        "image_id":int(current_object_id) ,
                        "category_id": int(item.label),
                        "area": int((item.bbox[3] - item.bbox[1]) * (item.bbox[2] - item.bbox[0])),
                        "color": "#979824",
                        "bbox": [int(item.bbox[0]), int(item.bbox[1]), \
                                 int(item.bbox[2] - item.bbox[0]), int(item.bbox[3] - item.bbox[1])],
                        "segmentation": [segment_info]
                    })
                self.annotation_id += 1
            with open(output_file, "w") as f:
                f.write(json.dumps(data))







if __name__ == "__main__":

    # specify the config file and checkpoint file here.
    config_file=rospy.get_param("config")
    checkpoint_file=rospy.get_param("checkpoint")

    # remove previous output
    rospack = rospkg.RosPack()
    path = rospack.get_path("swin_detection")
    output_multi_path=path+"/output_multi/"


    if os.path.exists(output_multi_path):
        shutil.rmtree(output_multi_path)

    rospy.loginfo("Initialization completed!")
    # ros initialization
    rospy.init_node("rosbag_catch_node")
    detector=Detection(config_file,checkpoint_file)

    rospy.spin()