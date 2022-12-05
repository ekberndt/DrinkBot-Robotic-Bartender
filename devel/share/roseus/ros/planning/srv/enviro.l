;; Auto-generated. Do not edit!


(when (boundp 'planning::enviro)
  (if (not (find-package "PLANNING"))
    (make-package "PLANNING"))
  (shadow 'enviro (find-package "PLANNING")))
(unless (find-package "PLANNING::ENVIRO")
  (make-package "PLANNING::ENVIRO"))
(unless (find-package "PLANNING::ENVIROREQUEST")
  (make-package "PLANNING::ENVIROREQUEST"))
(unless (find-package "PLANNING::ENVIRORESPONSE")
  (make-package "PLANNING::ENVIRORESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass planning::enviroRequest
  :super ros::object
  :slots (_obj_posx _obj_posy _obj_posz _obj_orientx _obj_orienty _obj_orientz _obj_orientw _sizex _sizey _sizez _name_obj _orient _goal ))

(defmethod planning::enviroRequest
  (:init
   (&key
    ((:obj_posx __obj_posx) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:obj_posy __obj_posy) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:obj_posz __obj_posz) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:obj_orientx __obj_orientx) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:obj_orienty __obj_orienty) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:obj_orientz __obj_orientz) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:obj_orientw __obj_orientw) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:sizex __sizex) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:sizey __sizey) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:sizez __sizez) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:name_obj __name_obj) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:orient __orient) nil)
    ((:goal __goal) (instance geometry_msgs::PoseStamped :init))
    )
   (send-super :init)
   (setq _obj_posx __obj_posx)
   (setq _obj_posy __obj_posy)
   (setq _obj_posz __obj_posz)
   (setq _obj_orientx __obj_orientx)
   (setq _obj_orienty __obj_orienty)
   (setq _obj_orientz __obj_orientz)
   (setq _obj_orientw __obj_orientw)
   (setq _sizex __sizex)
   (setq _sizey __sizey)
   (setq _sizez __sizez)
   (setq _name_obj __name_obj)
   (setq _orient __orient)
   (setq _goal __goal)
   self)
  (:obj_posx
   (&optional __obj_posx)
   (if __obj_posx (setq _obj_posx __obj_posx)) _obj_posx)
  (:obj_posy
   (&optional __obj_posy)
   (if __obj_posy (setq _obj_posy __obj_posy)) _obj_posy)
  (:obj_posz
   (&optional __obj_posz)
   (if __obj_posz (setq _obj_posz __obj_posz)) _obj_posz)
  (:obj_orientx
   (&optional __obj_orientx)
   (if __obj_orientx (setq _obj_orientx __obj_orientx)) _obj_orientx)
  (:obj_orienty
   (&optional __obj_orienty)
   (if __obj_orienty (setq _obj_orienty __obj_orienty)) _obj_orienty)
  (:obj_orientz
   (&optional __obj_orientz)
   (if __obj_orientz (setq _obj_orientz __obj_orientz)) _obj_orientz)
  (:obj_orientw
   (&optional __obj_orientw)
   (if __obj_orientw (setq _obj_orientw __obj_orientw)) _obj_orientw)
  (:sizex
   (&optional __sizex)
   (if __sizex (setq _sizex __sizex)) _sizex)
  (:sizey
   (&optional __sizey)
   (if __sizey (setq _sizey __sizey)) _sizey)
  (:sizez
   (&optional __sizez)
   (if __sizez (setq _sizez __sizez)) _sizez)
  (:name_obj
   (&optional __name_obj)
   (if __name_obj (setq _name_obj __name_obj)) _name_obj)
  (:orient
   (&optional (__orient :null))
   (if (not (eq __orient :null)) (setq _orient __orient)) _orient)
  (:goal
   (&rest __goal)
   (if (keywordp (car __goal))
       (send* _goal __goal)
     (progn
       (if __goal (setq _goal (car __goal)))
       _goal)))
  (:serialization-length
   ()
   (+
    ;; float32[] _obj_posx
    (* 4    (length _obj_posx)) 4
    ;; float32[] _obj_posy
    (* 4    (length _obj_posy)) 4
    ;; float32[] _obj_posz
    (* 4    (length _obj_posz)) 4
    ;; float32[] _obj_orientx
    (* 4    (length _obj_orientx)) 4
    ;; float32[] _obj_orienty
    (* 4    (length _obj_orienty)) 4
    ;; float32[] _obj_orientz
    (* 4    (length _obj_orientz)) 4
    ;; float32[] _obj_orientw
    (* 4    (length _obj_orientw)) 4
    ;; float32[] _sizex
    (* 4    (length _sizex)) 4
    ;; float32[] _sizey
    (* 4    (length _sizey)) 4
    ;; float32[] _sizez
    (* 4    (length _sizez)) 4
    ;; string[] _name_obj
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _name_obj)) 4
    ;; bool _orient
    1
    ;; geometry_msgs/PoseStamped _goal
    (send _goal :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _obj_posx
     (write-long (length _obj_posx) s)
     (dotimes (i (length _obj_posx))
       (sys::poke (elt _obj_posx i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _obj_posy
     (write-long (length _obj_posy) s)
     (dotimes (i (length _obj_posy))
       (sys::poke (elt _obj_posy i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _obj_posz
     (write-long (length _obj_posz) s)
     (dotimes (i (length _obj_posz))
       (sys::poke (elt _obj_posz i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _obj_orientx
     (write-long (length _obj_orientx) s)
     (dotimes (i (length _obj_orientx))
       (sys::poke (elt _obj_orientx i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _obj_orienty
     (write-long (length _obj_orienty) s)
     (dotimes (i (length _obj_orienty))
       (sys::poke (elt _obj_orienty i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _obj_orientz
     (write-long (length _obj_orientz) s)
     (dotimes (i (length _obj_orientz))
       (sys::poke (elt _obj_orientz i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _obj_orientw
     (write-long (length _obj_orientw) s)
     (dotimes (i (length _obj_orientw))
       (sys::poke (elt _obj_orientw i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _sizex
     (write-long (length _sizex) s)
     (dotimes (i (length _sizex))
       (sys::poke (elt _sizex i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _sizey
     (write-long (length _sizey) s)
     (dotimes (i (length _sizey))
       (sys::poke (elt _sizey i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _sizez
     (write-long (length _sizez) s)
     (dotimes (i (length _sizez))
       (sys::poke (elt _sizez i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; string[] _name_obj
     (write-long (length _name_obj) s)
     (dolist (elem _name_obj)
       (write-long (length elem) s) (princ elem s)
       )
     ;; bool _orient
       (if _orient (write-byte -1 s) (write-byte 0 s))
     ;; geometry_msgs/PoseStamped _goal
       (send _goal :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _obj_posx
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_posx (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _obj_posx i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _obj_posy
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_posy (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _obj_posy i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _obj_posz
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_posz (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _obj_posz i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _obj_orientx
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_orientx (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _obj_orientx i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _obj_orienty
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_orienty (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _obj_orienty i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _obj_orientz
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_orientz (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _obj_orientz i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _obj_orientw
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_orientw (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _obj_orientw i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _sizex
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _sizex (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _sizex i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _sizey
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _sizey (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _sizey i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _sizez
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _sizez (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _sizez i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; string[] _name_obj
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _name_obj (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _name_obj i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; bool _orient
     (setq _orient (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; geometry_msgs/PoseStamped _goal
     (send _goal :deserialize buf ptr-) (incf ptr- (send _goal :serialization-length))
   ;;
   self)
  )

(defclass planning::enviroResponse
  :super ros::object
  :slots (_response ))

(defmethod planning::enviroResponse
  (:init
   (&key
    ((:response __response) "")
    )
   (send-super :init)
   (setq _response (string __response))
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; string _response
    4 (length _response)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _response
       (write-long (length _response) s) (princ _response s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _response
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _response (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass planning::enviro
  :super ros::object
  :slots ())

(setf (get planning::enviro :md5sum-) "7057eb40c64cbf8bdf2c3deb4aec57bb")
(setf (get planning::enviro :datatype-) "planning/enviro")
(setf (get planning::enviro :request) planning::enviroRequest)
(setf (get planning::enviro :response) planning::enviroResponse)

(defmethod planning::enviroRequest
  (:response () (instance planning::enviroResponse :init)))

(setf (get planning::enviroRequest :md5sum-) "7057eb40c64cbf8bdf2c3deb4aec57bb")
(setf (get planning::enviroRequest :datatype-) "planning/enviroRequest")
(setf (get planning::enviroRequest :definition-)
      "# Request message types
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
bool orient

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
---
# Response message types
string response

")

(setf (get planning::enviroResponse :md5sum-) "7057eb40c64cbf8bdf2c3deb4aec57bb")
(setf (get planning::enviroResponse :datatype-) "planning/enviroResponse")
(setf (get planning::enviroResponse :definition-)
      "# Request message types
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
bool orient

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
---
# Response message types
string response

")



(provide :planning/enviro "7057eb40c64cbf8bdf2c3deb4aec57bb")


