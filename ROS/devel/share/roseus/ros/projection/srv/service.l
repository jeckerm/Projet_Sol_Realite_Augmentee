;; Auto-generated. Do not edit!


(when (boundp 'projection::service)
  (if (not (find-package "PROJECTION"))
    (make-package "PROJECTION"))
  (shadow 'service (find-package "PROJECTION")))
(unless (find-package "PROJECTION::SERVICE")
  (make-package "PROJECTION::SERVICE"))
(unless (find-package "PROJECTION::SERVICEREQUEST")
  (make-package "PROJECTION::SERVICEREQUEST"))
(unless (find-package "PROJECTION::SERVICERESPONSE")
  (make-package "PROJECTION::SERVICERESPONSE"))

(in-package "ROS")





(defclass projection::serviceRequest
  :super ros::object
  :slots (_L ))

(defmethod projection::serviceRequest
  (:init
   (&key
    ((:L __L) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _L __L)
   self)
  (:L
   (&optional __L)
   (if __L (setq _L __L)) _L)
  (:serialization-length
   ()
   (+
    ;; int64[] _L
    (* 8    (length _L)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64[] _L
     (write-long (length _L) s)
     (dotimes (i (length _L))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _L i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _L i)) (= (length ((elt _L i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _L i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _L i) . bv) 1) -1) s))
             ((and (class (elt _L i)) (= (length ((elt _L i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _L i) . bv) 0) s)
              (write-long (if (>= (elt _L i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _L i) s)(write-long (if (>= (elt _L i) 0) 0 #xffffffff) s)))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64[] _L
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _L (instantiate integer-vector n))
     (dotimes (i n)
#+(or :alpha :irix6 :x86_64)
      (setf (elt _L i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _L i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;;
   self)
  )

(defclass projection::serviceResponse
  :super ros::object
  :slots ())

(defmethod projection::serviceResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass projection::service
  :super ros::object
  :slots ())

(setf (get projection::service :md5sum-) "3c2cc25d6004da2681799b24f2e02ab6")
(setf (get projection::service :datatype-) "projection/service")
(setf (get projection::service :request) projection::serviceRequest)
(setf (get projection::service :response) projection::serviceResponse)

(defmethod projection::serviceRequest
  (:response () (instance projection::serviceResponse :init)))

(setf (get projection::serviceRequest :md5sum-) "3c2cc25d6004da2681799b24f2e02ab6")
(setf (get projection::serviceRequest :datatype-) "projection/serviceRequest")
(setf (get projection::serviceRequest :definition-)
      "int64[] L
---

")

(setf (get projection::serviceResponse :md5sum-) "3c2cc25d6004da2681799b24f2e02ab6")
(setf (get projection::serviceResponse :datatype-) "projection/serviceResponse")
(setf (get projection::serviceResponse :definition-)
      "int64[] L
---

")



(provide :projection/service "3c2cc25d6004da2681799b24f2e02ab6")


