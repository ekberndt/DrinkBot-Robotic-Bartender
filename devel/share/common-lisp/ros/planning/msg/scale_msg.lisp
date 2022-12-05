; Auto-generated. Do not edit!


(cl:in-package planning-msg)


;//! \htmlinclude scale_msg.msg.html

(cl:defclass <scale_msg> (roslisp-msg-protocol:ros-message)
  ((mass
    :reader mass
    :initarg :mass
    :type cl:float
    :initform 0.0))
)

(cl:defclass scale_msg (<scale_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <scale_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'scale_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name planning-msg:<scale_msg> is deprecated: use planning-msg:scale_msg instead.")))

(cl:ensure-generic-function 'mass-val :lambda-list '(m))
(cl:defmethod mass-val ((m <scale_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planning-msg:mass-val is deprecated.  Use planning-msg:mass instead.")
  (mass m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <scale_msg>) ostream)
  "Serializes a message object of type '<scale_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'mass))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <scale_msg>) istream)
  "Deserializes a message object of type '<scale_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mass) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<scale_msg>)))
  "Returns string type for a message object of type '<scale_msg>"
  "planning/scale_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'scale_msg)))
  "Returns string type for a message object of type 'scale_msg"
  "planning/scale_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<scale_msg>)))
  "Returns md5sum for a message object of type '<scale_msg>"
  "bc896cc245a01cb882740a335971513f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'scale_msg)))
  "Returns md5sum for a message object of type 'scale_msg"
  "bc896cc245a01cb882740a335971513f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<scale_msg>)))
  "Returns full string definition for message of type '<scale_msg>"
  (cl:format cl:nil "float32 mass~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'scale_msg)))
  "Returns full string definition for message of type 'scale_msg"
  (cl:format cl:nil "float32 mass~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <scale_msg>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <scale_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'scale_msg
    (cl:cons ':mass (mass msg))
))
