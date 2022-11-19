// Auto-generated. Do not edit!

// (in-package planning.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class enviroRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.obj_posx = null;
      this.obj_posy = null;
      this.obj_posz = null;
      this.obj_orientx = null;
      this.obj_orienty = null;
      this.obj_orientz = null;
      this.obj_orientw = null;
      this.sizex = null;
      this.sizey = null;
      this.sizez = null;
      this.name_obj = null;
      this.goal = null;
    }
    else {
      if (initObj.hasOwnProperty('obj_posx')) {
        this.obj_posx = initObj.obj_posx
      }
      else {
        this.obj_posx = [];
      }
      if (initObj.hasOwnProperty('obj_posy')) {
        this.obj_posy = initObj.obj_posy
      }
      else {
        this.obj_posy = [];
      }
      if (initObj.hasOwnProperty('obj_posz')) {
        this.obj_posz = initObj.obj_posz
      }
      else {
        this.obj_posz = [];
      }
      if (initObj.hasOwnProperty('obj_orientx')) {
        this.obj_orientx = initObj.obj_orientx
      }
      else {
        this.obj_orientx = [];
      }
      if (initObj.hasOwnProperty('obj_orienty')) {
        this.obj_orienty = initObj.obj_orienty
      }
      else {
        this.obj_orienty = [];
      }
      if (initObj.hasOwnProperty('obj_orientz')) {
        this.obj_orientz = initObj.obj_orientz
      }
      else {
        this.obj_orientz = [];
      }
      if (initObj.hasOwnProperty('obj_orientw')) {
        this.obj_orientw = initObj.obj_orientw
      }
      else {
        this.obj_orientw = [];
      }
      if (initObj.hasOwnProperty('sizex')) {
        this.sizex = initObj.sizex
      }
      else {
        this.sizex = [];
      }
      if (initObj.hasOwnProperty('sizey')) {
        this.sizey = initObj.sizey
      }
      else {
        this.sizey = [];
      }
      if (initObj.hasOwnProperty('sizez')) {
        this.sizez = initObj.sizez
      }
      else {
        this.sizez = [];
      }
      if (initObj.hasOwnProperty('name_obj')) {
        this.name_obj = initObj.name_obj
      }
      else {
        this.name_obj = [];
      }
      if (initObj.hasOwnProperty('goal')) {
        this.goal = initObj.goal
      }
      else {
        this.goal = new geometry_msgs.msg.PoseStamped();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type enviroRequest
    // Serialize message field [obj_posx]
    bufferOffset = _arraySerializer.float32(obj.obj_posx, buffer, bufferOffset, null);
    // Serialize message field [obj_posy]
    bufferOffset = _arraySerializer.float32(obj.obj_posy, buffer, bufferOffset, null);
    // Serialize message field [obj_posz]
    bufferOffset = _arraySerializer.float32(obj.obj_posz, buffer, bufferOffset, null);
    // Serialize message field [obj_orientx]
    bufferOffset = _arraySerializer.float32(obj.obj_orientx, buffer, bufferOffset, null);
    // Serialize message field [obj_orienty]
    bufferOffset = _arraySerializer.float32(obj.obj_orienty, buffer, bufferOffset, null);
    // Serialize message field [obj_orientz]
    bufferOffset = _arraySerializer.float32(obj.obj_orientz, buffer, bufferOffset, null);
    // Serialize message field [obj_orientw]
    bufferOffset = _arraySerializer.float32(obj.obj_orientw, buffer, bufferOffset, null);
    // Serialize message field [sizex]
    bufferOffset = _arraySerializer.float32(obj.sizex, buffer, bufferOffset, null);
    // Serialize message field [sizey]
    bufferOffset = _arraySerializer.float32(obj.sizey, buffer, bufferOffset, null);
    // Serialize message field [sizez]
    bufferOffset = _arraySerializer.float32(obj.sizez, buffer, bufferOffset, null);
    // Serialize message field [name_obj]
    bufferOffset = _arraySerializer.string(obj.name_obj, buffer, bufferOffset, null);
    // Serialize message field [goal]
    bufferOffset = geometry_msgs.msg.PoseStamped.serialize(obj.goal, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type enviroRequest
    let len;
    let data = new enviroRequest(null);
    // Deserialize message field [obj_posx]
    data.obj_posx = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [obj_posy]
    data.obj_posy = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [obj_posz]
    data.obj_posz = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [obj_orientx]
    data.obj_orientx = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [obj_orienty]
    data.obj_orienty = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [obj_orientz]
    data.obj_orientz = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [obj_orientw]
    data.obj_orientw = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [sizex]
    data.sizex = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [sizey]
    data.sizey = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [sizez]
    data.sizez = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [name_obj]
    data.name_obj = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [goal]
    data.goal = geometry_msgs.msg.PoseStamped.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.obj_posx.length;
    length += 4 * object.obj_posy.length;
    length += 4 * object.obj_posz.length;
    length += 4 * object.obj_orientx.length;
    length += 4 * object.obj_orienty.length;
    length += 4 * object.obj_orientz.length;
    length += 4 * object.obj_orientw.length;
    length += 4 * object.sizex.length;
    length += 4 * object.sizey.length;
    length += 4 * object.sizez.length;
    object.name_obj.forEach((val) => {
      length += 4 + _getByteLength(val);
    });
    length += geometry_msgs.msg.PoseStamped.getMessageSize(object.goal);
    return length + 44;
  }

  static datatype() {
    // Returns string type for a service object
    return 'planning/enviroRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f753f1d4d2bf2e618dfa1eac6125eedf';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Request message types
    float32[] obj_posx
    float32[] obj_posy
    float32[] obj_posz
    float32[] obj_orientx
    float32[] obj_orienty
    float32[] obj_orientz
    float32[] obj_orientw
    float32[] sizex
    float32[] sizey
    float32[] sizez
    string[] name_obj
    
    geometry_msgs/PoseStamped goal
    
    
    ================================================================================
    MSG: geometry_msgs/PoseStamped
    # A Pose with reference coordinate frame and timestamp
    Header header
    Pose pose
    
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
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new enviroRequest(null);
    if (msg.obj_posx !== undefined) {
      resolved.obj_posx = msg.obj_posx;
    }
    else {
      resolved.obj_posx = []
    }

    if (msg.obj_posy !== undefined) {
      resolved.obj_posy = msg.obj_posy;
    }
    else {
      resolved.obj_posy = []
    }

    if (msg.obj_posz !== undefined) {
      resolved.obj_posz = msg.obj_posz;
    }
    else {
      resolved.obj_posz = []
    }

    if (msg.obj_orientx !== undefined) {
      resolved.obj_orientx = msg.obj_orientx;
    }
    else {
      resolved.obj_orientx = []
    }

    if (msg.obj_orienty !== undefined) {
      resolved.obj_orienty = msg.obj_orienty;
    }
    else {
      resolved.obj_orienty = []
    }

    if (msg.obj_orientz !== undefined) {
      resolved.obj_orientz = msg.obj_orientz;
    }
    else {
      resolved.obj_orientz = []
    }

    if (msg.obj_orientw !== undefined) {
      resolved.obj_orientw = msg.obj_orientw;
    }
    else {
      resolved.obj_orientw = []
    }

    if (msg.sizex !== undefined) {
      resolved.sizex = msg.sizex;
    }
    else {
      resolved.sizex = []
    }

    if (msg.sizey !== undefined) {
      resolved.sizey = msg.sizey;
    }
    else {
      resolved.sizey = []
    }

    if (msg.sizez !== undefined) {
      resolved.sizez = msg.sizez;
    }
    else {
      resolved.sizez = []
    }

    if (msg.name_obj !== undefined) {
      resolved.name_obj = msg.name_obj;
    }
    else {
      resolved.name_obj = []
    }

    if (msg.goal !== undefined) {
      resolved.goal = geometry_msgs.msg.PoseStamped.Resolve(msg.goal)
    }
    else {
      resolved.goal = new geometry_msgs.msg.PoseStamped()
    }

    return resolved;
    }
};

class enviroResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cmd = null;
    }
    else {
      if (initObj.hasOwnProperty('cmd')) {
        this.cmd = initObj.cmd
      }
      else {
        this.cmd = new geometry_msgs.msg.Twist();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type enviroResponse
    // Serialize message field [cmd]
    bufferOffset = geometry_msgs.msg.Twist.serialize(obj.cmd, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type enviroResponse
    let len;
    let data = new enviroResponse(null);
    // Deserialize message field [cmd]
    data.cmd = geometry_msgs.msg.Twist.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a service object
    return 'planning/enviroResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a0c47a2b42626c8e0bd2a277053c6c62';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Response message types
    geometry_msgs/Twist cmd
    
    
    ================================================================================
    MSG: geometry_msgs/Twist
    # This expresses velocity in free space broken into its linear and angular parts.
    Vector3  linear
    Vector3  angular
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new enviroResponse(null);
    if (msg.cmd !== undefined) {
      resolved.cmd = geometry_msgs.msg.Twist.Resolve(msg.cmd)
    }
    else {
      resolved.cmd = new geometry_msgs.msg.Twist()
    }

    return resolved;
    }
};

module.exports = {
  Request: enviroRequest,
  Response: enviroResponse,
  md5sum() { return '7db6d4836f25ca96fe8ff3e313a5f71c'; },
  datatype() { return 'planning/enviro'; }
};
