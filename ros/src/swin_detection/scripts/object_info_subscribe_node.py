#! /usr/bin/env python3
import rospy
import rospkg
from swin_detection.msg import Object
from sensor_msgs.msg import Image
import os
import json
import shutil
from cv_bridge import CvBridge, CvBridgeError
import cv2

#object-id table
object_id_table=[]

#{score:message} mapping dictionary
score_msg_map={}

#initalize annotation id
annotation_id=1


def do_msg(msg,args):
    data=args[0]
    output_file=args[1]
    path=args[2]

    global object_id_table
    global score_msg_map
    global annotation_id

    threshold=10
    margin=50

    # convert ros message to opencv format
    bridge = CvBridge()
    height,width,_=bridge.imgmsg_to_cv2(msg.image_rgb).shape

    image_prefix=path+"/images/"
    if not os.path.exists(image_prefix):
        os.mkdir(image_prefix)

    object_id=msg.id

    # make sure the centroid lie in the proper area instead of on the verge
    if msg.bbox[1] > margin and msg.bbox[3] < height-margin:
        object_table.append(object_id)

        if not object_id in score_msg_map.keys():
            score_msg_map[object_id]={}

            score_msg_map[object_id][msg.score]=msg
        else:
            score_msg_map[object_id][msg.score]=msg

    if(object_table.count(object_id)>threshold and (not -1 in score_msg_map[object_id].keys())):
        score_msg_map[object_id][-1]=0

        current_msg = score_msg_map[object_id][max(score_msg_map[object_id].keys())]
        rospy.loginfo(current_msg.bbox)
        # "image part"
        #
        # "save image"
        image_name="frame"+f"{msg.id}".zfill(6)+".png"
        image_msg=current_msg.image_rgb

        image=bridge.imgmsg_to_cv2(image_msg)
        cv2.imwrite(image_prefix+image_name,image)

        # "write image information"
        data["images"].append({"id": current_msg.id,"width":width,"height":height,
                              "file_name":"images/"+image_name})



        if not current_msg.category_id in [item["id"] for item in data["categories"]]:
            data["categories"].append({"id":current_msg.category_id,"name": current_msg.name})

        # "annotation part"

        data["annotations"].append({
            "id":annotation_id,
            "image_id":current_msg.id,
            "category_id":current_msg.category_id,
            "area":(current_msg.bbox[3]-current_msg.bbox[1])*(current_msg.bbox[2]-current_msg.bbox[0]),
            "color":"#979824",
            "bbox": [current_msg.bbox[0],current_msg.bbox[1],\
                     current_msg.bbox[2]-current_msg.bbox[0],current_msg.bbox[3]-current_msg.bbox[1]],
            "segmentation": [current_msg.segm]})

        with open(output_file, "w") as f:
            f.write(json.dumps(data))

        annotation_id+=1



if __name__ == "__main__":

    #declare the output directory
    rospack = rospkg.RosPack()
    rospy.init_node("subscribe_object_info_node")
    path=rospack.get_path("swin_detection")

    path=path+"/output"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    output_file=path+"/annotations.json"


    #initialize the json file
    data={}
    data["info"] = []
    data['images']=[]
    data['annotations']=[]
    data['categories']=[]

    data["licenses"]=[]

    if not os.path.exists(output_file):

        with open(output_file,"w") as f:
            f.write(json.dumps(data))

    object_table=[]
    sub=rospy.Subscriber("/test_info",Object,do_msg,queue_size=1000,callback_args=(data,output_file,path))

    rospy.spin()