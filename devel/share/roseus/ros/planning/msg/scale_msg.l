;; Auto-generated. Do not edit!


(when (boundp 'planning::scale_msg)
  (if (not (find-package "PLANNING"))
    (make-package "PLANNING"))
  (shadow 'scale_msg (find-package "PLANNING")))
(unless (find-package "PLANNING::SCALE_MSG")
  (make-package "PLANNING::SCALE_MSG"))

(in-package "ROS")
;;//! \htmlinclude scale_msg.msg.html


(defclass planning::scale_msg
  :super ros::object
  :slots (_mass ))

(defmethod planning::scale_msg
  (:init
   (&key
    ((:mass __mass) 0.0)
    )
   (send-super :init)
   (setq _mass (float __mass))
   self)
  (:mass
   (&optional __mass)
   (if __mass (setq _mass __mass)) _mass)
  (:serialization-length
   ()
   (+
    ;; float32 _mass
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _mass
       (sys::poke _mass (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _mass
     (setq _mass (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get planning::scale_msg :md5sum-) "bc896cc245a01cb882740a335971513f")
(setf (get planning::scale_msg :datatype-) "planning/scale_msg")
(setf (get planning::scale_msg :definition-)
      "float32 mass
")



(provide :planning/scale_msg "bc896cc245a01cb882740a335971513f")


