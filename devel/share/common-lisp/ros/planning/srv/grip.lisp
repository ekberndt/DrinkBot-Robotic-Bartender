; Auto-generated. Do not edit!


(cl:in-package planning-srv)


;//! \htmlinclude grip-request.msg.html

(cl:defclass <grip-request> (roslisp-msg-protocol:ros-message)
  ((grip
    :reader grip
    :initarg :grip
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass grip-request (<grip-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <grip-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'grip-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name planning-srv:<grip-request> is deprecated: use planning-srv:grip-request instead.")))

(cl:ensure-generic-function 'grip-val :lambda-list '(m))
(cl:defmethod grip-val ((m <grip-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planning-srv:grip-val is deprecated.  Use planning-srv:grip instead.")
  (grip m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <grip-request>) ostream)
  "Serializes a message object of type '<grip-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'grip) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <grip-request>) istream)
  "Deserializes a message object of type '<grip-request>"
    (cl:setf (cl:slot-value msg 'grip) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<grip-request>)))
  "Returns string type for a service object of type '<grip-request>"
  "planning/gripRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'grip-request)))
  "Returns string type for a service object of type 'grip-request"
  "planning/gripRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<grip-request>)))
  "Returns md5sum for a message object of type '<grip-request>"
  "f1efe09e5c849855890b1b914a2c218c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'grip-request)))
  "Returns md5sum for a message object of type 'grip-request"
  "f1efe09e5c849855890b1b914a2c218c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<grip-request>)))
  "Returns full string definition for message of type '<grip-request>"
  (cl:format cl:nil "# Request message types~%bool grip~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'grip-request)))
  "Returns full string definition for message of type 'grip-request"
  (cl:format cl:nil "# Request message types~%bool grip~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <grip-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <grip-request>))
  "Converts a ROS message object to a list"
  (cl:list 'grip-request
    (cl:cons ':grip (grip msg))
))
;//! \htmlinclude grip-response.msg.html

(cl:defclass <grip-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:string
    :initform ""))
)

(cl:defclass grip-response (<grip-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <grip-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'grip-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name planning-srv:<grip-response> is deprecated: use planning-srv:grip-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <grip-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planning-srv:response-val is deprecated.  Use planning-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <grip-response>) ostream)
  "Serializes a message object of type '<grip-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'response))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'response))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <grip-response>) istream)
  "Deserializes a message object of type '<grip-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'response) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'response) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<grip-response>)))
  "Returns string type for a service object of type '<grip-response>"
  "planning/gripResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'grip-response)))
  "Returns string type for a service object of type 'grip-response"
  "planning/gripResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<grip-response>)))
  "Returns md5sum for a message object of type '<grip-response>"
  "f1efe09e5c849855890b1b914a2c218c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'grip-response)))
  "Returns md5sum for a message object of type 'grip-response"
  "f1efe09e5c849855890b1b914a2c218c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<grip-response>)))
  "Returns full string definition for message of type '<grip-response>"
  (cl:format cl:nil "# Response message types~%string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'grip-response)))
  "Returns full string definition for message of type 'grip-response"
  (cl:format cl:nil "# Response message types~%string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <grip-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'response))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <grip-response>))
  "Converts a ROS message object to a list"
  (cl:list 'grip-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'grip)))
  'grip-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'grip)))
  'grip-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'grip)))
  "Returns string type for a service object of type '<grip>"
  "planning/grip")