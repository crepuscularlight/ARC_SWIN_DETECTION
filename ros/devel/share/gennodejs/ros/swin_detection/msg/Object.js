// Auto-generated. Do not edit!

// (in-package swin_detection.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class Object {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.time = null;
      this.place = null;
      this.name = null;
      this.category_id = null;
      this.id = null;
      this.cropped_image = null;
      this.image_rgb = null;
      this.bbox = null;
      this.segm = null;
      this.score = null;
    }
    else {
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = '';
      }
      if (initObj.hasOwnProperty('place')) {
        this.place = initObj.place
      }
      else {
        this.place = '';
      }
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('category_id')) {
        this.category_id = initObj.category_id
      }
      else {
        this.category_id = 0;
      }
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('cropped_image')) {
        this.cropped_image = initObj.cropped_image
      }
      else {
        this.cropped_image = new sensor_msgs.msg.Image();
      }
      if (initObj.hasOwnProperty('image_rgb')) {
        this.image_rgb = initObj.image_rgb
      }
      else {
        this.image_rgb = new sensor_msgs.msg.Image();
      }
      if (initObj.hasOwnProperty('bbox')) {
        this.bbox = initObj.bbox
      }
      else {
        this.bbox = [];
      }
      if (initObj.hasOwnProperty('segm')) {
        this.segm = initObj.segm
      }
      else {
        this.segm = [];
      }
      if (initObj.hasOwnProperty('score')) {
        this.score = initObj.score
      }
      else {
        this.score = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Object
    // Serialize message field [time]
    bufferOffset = _serializer.string(obj.time, buffer, bufferOffset);
    // Serialize message field [place]
    bufferOffset = _serializer.string(obj.place, buffer, bufferOffset);
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [category_id]
    bufferOffset = _serializer.uint16(obj.category_id, buffer, bufferOffset);
    // Serialize message field [id]
    bufferOffset = _serializer.uint16(obj.id, buffer, bufferOffset);
    // Serialize message field [cropped_image]
    bufferOffset = sensor_msgs.msg.Image.serialize(obj.cropped_image, buffer, bufferOffset);
    // Serialize message field [image_rgb]
    bufferOffset = sensor_msgs.msg.Image.serialize(obj.image_rgb, buffer, bufferOffset);
    // Serialize message field [bbox]
    bufferOffset = _arraySerializer.float64(obj.bbox, buffer, bufferOffset, null);
    // Serialize message field [segm]
    bufferOffset = _arraySerializer.float64(obj.segm, buffer, bufferOffset, null);
    // Serialize message field [score]
    bufferOffset = _serializer.float64(obj.score, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Object
    let len;
    let data = new Object(null);
    // Deserialize message field [time]
    data.time = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [place]
    data.place = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [category_id]
    data.category_id = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [id]
    data.id = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [cropped_image]
    data.cropped_image = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset);
    // Deserialize message field [image_rgb]
    data.image_rgb = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset);
    // Deserialize message field [bbox]
    data.bbox = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [segm]
    data.segm = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [score]
    data.score = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.time);
    length += _getByteLength(object.place);
    length += _getByteLength(object.name);
    length += sensor_msgs.msg.Image.getMessageSize(object.cropped_image);
    length += sensor_msgs.msg.Image.getMessageSize(object.image_rgb);
    length += 8 * object.bbox.length;
    length += 8 * object.segm.length;
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'swin_detection/Object';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '46fa9eed002d6f2c7842f29306634525';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string time
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Object(null);
    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = ''
    }

    if (msg.place !== undefined) {
      resolved.place = msg.place;
    }
    else {
      resolved.place = ''
    }

    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.category_id !== undefined) {
      resolved.category_id = msg.category_id;
    }
    else {
      resolved.category_id = 0
    }

    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.cropped_image !== undefined) {
      resolved.cropped_image = sensor_msgs.msg.Image.Resolve(msg.cropped_image)
    }
    else {
      resolved.cropped_image = new sensor_msgs.msg.Image()
    }

    if (msg.image_rgb !== undefined) {
      resolved.image_rgb = sensor_msgs.msg.Image.Resolve(msg.image_rgb)
    }
    else {
      resolved.image_rgb = new sensor_msgs.msg.Image()
    }

    if (msg.bbox !== undefined) {
      resolved.bbox = msg.bbox;
    }
    else {
      resolved.bbox = []
    }

    if (msg.segm !== undefined) {
      resolved.segm = msg.segm;
    }
    else {
      resolved.segm = []
    }

    if (msg.score !== undefined) {
      resolved.score = msg.score;
    }
    else {
      resolved.score = 0.0
    }

    return resolved;
    }
};

module.exports = Object;
