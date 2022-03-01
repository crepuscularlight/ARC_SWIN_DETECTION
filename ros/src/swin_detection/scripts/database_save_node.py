#! /usr/bin/env python3
import rospy
import rospkg
from swin_detection.msg import Object
from sensor_msgs.msg import Image
import os
import json
from cv_bridge import CvBridge, CvBridgeError
import cv2
import shutil

object_id_table=[]
score_msg_map={}
annotation_id=1
def do_msg(msg,args):

    database_dir=args

    global object_id_table
    global score_msg_map
    global annotation_id

    threshold=10
    bridge = CvBridge()
    # database_dir=os.path.abspath(".")+"/src/swin_detection/output/database_images/"
    if not os.path.exists(database_dir):
        os.mkdir(database_dir)

    object_id=msg.id

    # object_table.append(object_id)
    if msg.bbox[1] > 50 and msg.bbox[3] < 350:
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

        padding=10
        x1,y1,x2,y2=current_msg.bbox

        x1=int(x1-padding) if x1-10>0 else 0
        y1=int(y1-padding) if y1-10>0 else 0
        x2=int(x2+padding) if x2+10<640 else 640
        y2=int(y2+padding) if y2+10<480 else 480



        data={}
        data["time"]=current_msg.time
        data["location"]=current_msg.place
        data["object_id"]=current_msg.id
        data["category"]=current_msg.name
        data["category_id"]=current_msg.category_id

        data["bbox"]=[current_msg.bbox[0]-x1,
                      current_msg.bbox[1]-y1,
                      current_msg.bbox[2]-x1,
                      current_msg.bbox[3]-y1]
        data["segm"]=[]
        data["image"]={}
        data["image"]["height"]=y2-y1
        data["image"]["width"]=x2-x1
        for i in range(len(current_msg.segm)):
            if i%2==0:
                data["segm"].append(current_msg.segm[i]-x1)
            else:
                data["segm"].append(current_msg.segm[i]-y1)

        data["score"]=current_msg.score

        image_name="frame"+f"{msg.id}".zfill(6)
        data["image"]["name"]=image_name
        output_file=database_dir+image_name+".json"
        rospy.loginfo(database_dir)
        rospy.loginfo(output_file)
        with open(output_file, "w") as f:
            f.write(json.dumps(data))
        image_msg=current_msg.image_rgb
        image=bridge.imgmsg_to_cv2(image_msg)
        rospy.loginfo(database_dir+image_name+".png")
        cv2.imwrite(database_dir+image_name+".png",image[y1:y2,x1:x2])


    image_msg=msg.cropped_image
    pub=rospy.Publisher("/cropped_image",Image,queue_size=1000)
    pub.publish(image_msg)






if __name__ == "__main__":

    rospack = rospkg.RosPack()
    path=rospack.get_path("swin_detection")


    rospy.init_node("database_save_node")



    path=path+"/output_database/"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    output_path=path

    # if not os.path.exists(output_path):
    #     os.mkdir(output_path)


    object_table=[]
    sub=rospy.Subscriber("/test_info",Object,do_msg,queue_size=1000,callback_args=(output_path))

    rospy.spin()