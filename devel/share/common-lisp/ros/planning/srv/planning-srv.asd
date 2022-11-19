
(cl:in-package :asdf)

(defsystem "planning-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "enviro" :depends-on ("_package_enviro"))
    (:file "_package_enviro" :depends-on ("_package"))
  ))