
(cl:in-package :asdf)

(defsystem "planning-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "scale_msg" :depends-on ("_package_scale_msg"))
    (:file "_package_scale_msg" :depends-on ("_package"))
  ))