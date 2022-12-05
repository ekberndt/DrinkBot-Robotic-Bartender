;; Auto-generated. Do not edit!


(when (boundp 'planning::grip)
  (if (not (find-package "PLANNING"))
    (make-package "PLANNING"))
  (shadow 'grip (find-package "PLANNING")))
(unless (find-package "PLANNING::GRIP")
  (make-package "PLANNING::GRIP"))
(unless (find-package "PLANNING::GRIPREQUEST")
  (make-package "PLANNING::GRIPREQUEST"))
(unless (find-package "PLANNING::GRIPRESPONSE")
  (make-package "PLANNING::GRIPRESPONSE"))

(in-package "ROS")





(defclass planning::gripRequest
  :super ros::object
  :slots (_grip ))

(defmethod planning::gripRequest
  (:init
   (&key
    ((:grip __grip) nil)
    )
   (send-super :init)
   (setq _grip __grip)
   self)
  (:grip
   (&optional (__grip :null))
   (if (not (eq __grip :null)) (setq _grip __grip)) _grip)
  (:serialization-length
   ()
   (+
    ;; bool _grip
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _grip
       (if _grip (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _grip
     (setq _grip (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass planning::gripResponse
  :super ros::object
  :slots (_response ))

(defmethod planning::gripResponse
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

(defclass planning::grip
  :super ros::object
  :slots ())

(setf (get planning::grip :md5sum-) "f1efe09e5c849855890b1b914a2c218c")
(setf (get planning::grip :datatype-) "planning/grip")
(setf (get planning::grip :request) planning::gripRequest)
(setf (get planning::grip :response) planning::gripResponse)

(defmethod planning::gripRequest
  (:response () (instance planning::gripResponse :init)))

(setf (get planning::gripRequest :md5sum-) "f1efe09e5c849855890b1b914a2c218c")
(setf (get planning::gripRequest :datatype-) "planning/gripRequest")
(setf (get planning::gripRequest :definition-)
      "# Request message types
bool grip

---
# Response message types
string response
")

(setf (get planning::gripResponse :md5sum-) "f1efe09e5c849855890b1b914a2c218c")
(setf (get planning::gripResponse :datatype-) "planning/gripResponse")
(setf (get planning::gripResponse :definition-)
      "# Request message types
bool grip

---
# Response message types
string response
")



(provide :planning/grip "f1efe09e5c849855890b1b914a2c218c")


