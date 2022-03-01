import numpy as np
import  cv2
import rospy

# Given object mask return the contour
def extract_boundary(mask):
    mask = mask.astype(np.uint8)
    contour, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    tmp = np.array(contour[0])
    tmp = np.squeeze(tmp, axis=1)
    tmp = tmp.flatten()

    return contour, tmp

#The class to store the object information
class ObjectInfo:
    def __init__(self,label,bbox,mask,id):
        """
        label:the class id
        bbox:bounding box
        score:prediction probability
        mask:instance segmentation mask
        id:object id
        segment_points:annotations segment points
        """
        self.label=label
        self.bbox=bbox
        self.score=bbox[-1]
        self.mask=mask
        self.id=id
        _,self.segment_points=extract_boundary(self.mask)


#class to store the image information
class ImageInfo:
    def __init__(self,bboxes,segms,labels,correspondances,img):
        """
        bboxes:all object bounding boxes
        segms:all object segmentation information
        labels:all object class id
        correspondances:all bounding box relation with object id
        img:rgb images
        object_info_list:
        id_list:appeared id list
        """
        self.bboxes=bboxes
        self.segms=segms
        self.labels=labels
        self.correspondances=correspondances
        self.img=img
        self.object_info_list=[]
        self.id_list=[]


    def split(self):
        for i, (bbox, label) in enumerate(zip(self.bboxes, self.labels)):
            if i>=len(self.correspondances):
                continue
            bbox_int = bbox.astype(np.int32)
            mask=self.segms[i]
            obj=ObjectInfo(label,bbox_int,mask,self.correspondances[i][1]+1)
            self.object_info_list.append(obj)
            self.id_list.append(obj.id)


#class to find the optimal annotation image
class ImageTable:
    def __init__(self):
        self.image_info_list=[]
        self.id_dict={}
        self.id_score_image_map={}
        self.id_window=[]
        self.horrizon=120

    def add(self,image_info):
        if len(self.image_info_list)<self.horrizon:
            self.image_info_list.append(image_info)
        else:
            self.image_info_list.pop(0)
            self.image_info_list.append(image_info)

        # id_list=[]

        for item in image_info.object_info_list:

            if item.id not in self.id_dict.keys():
                self.id_dict[item.id]=0
            if item.id not in self.id_score_image_map.keys():
                self.id_score_image_map[item.id]={}

            if item.bbox[1] > 50 and item.bbox[3] < 350:
                self.id_score_image_map[item.id][item.score]=image_info
                self.id_dict[item.id]+=1


    def select(self):

        threshold=6
        for object_id in self.image_info_list[-1].id_list:
            if(self.id_dict[object_id]>threshold and -1 not in self.id_score_image_map[object_id].keys()):
                self.id_score_image_map[object_id][-1]=0
                current_image=self.id_score_image_map[object_id][max(self.id_score_image_map[object_id].keys())]
                return current_image,object_id
        return None,None
