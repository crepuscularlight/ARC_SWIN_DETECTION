;; Auto-generated. Do not edit!


(when (boundp 'swin_detection::Object)
  (if (not (find-package "SWIN_DETECTION"))
    (make-package "SWIN_DETECTION"))
  (shadow 'Object (find-package "SWIN_DETECTION")))
(unless (find-package "SWIN_DETECTION::OBJECT")
  (make-package "SWIN_DETECTION::OBJECT"))

(in-package "ROS")
;;//! \htmlinclude Object.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass swin_detection::Object
  :super ros::object
  :slots (_time _place _name _category_id _id _cropped_image _image_rgb _bbox _segm _score ))

(defmethod swin_detection::Object
  (:init
   (&key
    ((:time __time) "")
    ((:place __place) "")
    ((:name __name) "")
    ((:category_id __category_id) 0)
    ((:id __id) 0)
    ((:cropped_image __cropped_image) (instance sensor_msgs::Image :init))
    ((:image_rgb __image_rgb) (instance sensor_msgs::Image :init))
    ((:bbox __bbox) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:segm __segm) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:score __score) 0.0)
    )
   (send-super :init)
   (setq _time (string __time))
   (setq _place (string __place))
   (setq _name (string __name))
   (setq _category_id (round __category_id))
   (setq _id (round __id))
   (setq _cropped_image __cropped_image)
   (setq _image_rgb __image_rgb)
   (setq _bbox __bbox)
   (setq _segm __segm)
   (setq _score (float __score))
   self)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:place
   (&optional __place)
   (if __place (setq _place __place)) _place)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:category_id
   (&optional __category_id)
   (if __category_id (setq _category_id __category_id)) _category_id)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:cropped_image
   (&rest __cropped_image)
   (if (keywordp (car __cropped_image))
       (send* _cropped_image __cropped_image)
     (progn
       (if __cropped_image (setq _cropped_image (car __cropped_image)))
       _cropped_image)))
  (:image_rgb
   (&rest __image_rgb)
   (if (keywordp (car __image_rgb))
       (send* _image_rgb __image_rgb)
     (progn
       (if __image_rgb (setq _image_rgb (car __image_rgb)))
       _image_rgb)))
  (:bbox
   (&optional __bbox)
   (if __bbox (setq _bbox __bbox)) _bbox)
  (:segm
   (&optional __segm)
   (if __segm (setq _segm __segm)) _segm)
  (:score
   (&optional __score)
   (if __score (setq _score __score)) _score)
  (:serialization-length
   ()
   (+
    ;; string _time
    4 (length _time)
    ;; string _place
    4 (length _place)
    ;; string _name
    4 (length _name)
    ;; uint16 _category_id
    2
    ;; uint16 _id
    2
    ;; sensor_msgs/Image _cropped_image
    (send _cropped_image :serialization-length)
    ;; sensor_msgs/Image _image_rgb
    (send _image_rgb :serialization-length)
    ;; float64[] _bbox
    (* 8    (length _bbox)) 4
    ;; float64[] _segm
    (* 8    (length _segm)) 4
    ;; float64 _score
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _time
       (write-long (length _time) s) (princ _time s)
     ;; string _place
       (write-long (length _place) s) (princ _place s)
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; uint16 _category_id
       (write-word _category_id s)
     ;; uint16 _id
       (write-word _id s)
     ;; sensor_msgs/Image _cropped_image
       (send _cropped_image :serialize s)
     ;; sensor_msgs/Image _image_rgb
       (send _image_rgb :serialize s)
     ;; float64[] _bbox
     (write-long (length _bbox) s)
     (dotimes (i (length _bbox))
       (sys::poke (elt _bbox i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _segm
     (write-long (length _segm) s)
     (dotimes (i (length _segm))
       (sys::poke (elt _segm i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _score
       (sys::poke _score (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _time
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _time (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _place
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _place (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint16 _category_id
     (setq _category_id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _id
     (setq _id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; sensor_msgs/Image _cropped_image
     (send _cropped_image :deserialize buf ptr-) (incf ptr- (send _cropped_image :serialization-length))
   ;; sensor_msgs/Image _image_rgb
     (send _image_rgb :deserialize buf ptr-) (incf ptr- (send _image_rgb :serialization-length))
   ;; float64[] _bbox
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bbox (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _bbox i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _segm
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _segm (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _segm i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _score
     (setq _score (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get swin_detection::Object :md5sum-) "46fa9eed002d6f2c7842f29306634525")
(setf (get swin_detection::Object :datatype-) "swin_detection/Object")
(setf (get swin_detection::Object :definition-)
      "string time
string place
string name
uint16 category_id
uint16 id
sensor_msgs/Image cropped_image
sensor_msgs/Image image_rgb
float64[] bbox
float64[] segm
float64 score



================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :swin_detection/Object "46fa9eed002d6f2c7842f29306634525")


