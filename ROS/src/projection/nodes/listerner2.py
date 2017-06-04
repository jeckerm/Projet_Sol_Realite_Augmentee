#!/usr/bin/env python  
import roslib
roslib.load_manifest('projection')
import rospy
import math
import tf
import geometry_msgs.msg
import tests_affichages
from geometry_msgs.msg import WrenchStamped

#def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #print("Valeur")
    #print(data.force[0])



def listener():
    print("je me lance")
    rospy.init_node('tf_listener')
    listener_tf = tf.TransformListener()
    rate = rospy.Rate(1.0)
    L = []
    #rospy.Subscriber("optoforce_1", WrenchStamped, callback)
    print("J'ai souscrit")
    #while not rospy.is_shutdown():
        #try:
    if listener_tf.frameExists('/base_link'):
        print("Existe")
        (trans,rot) = listener_tf.lookupTransform('base_link', '/world', rospy.Time(0)) #le temps de ce noeud bug ac le ros bag...
        print("Force")
        x =tests_affichages.fois_dix(trans[0])
        print(trans[0],x)
    else:
        print("NotExist")
#except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    #print("Exception")
    #continue

    #rate.sleep()
    rospy.spin()
    
if __name__ == '__main__':
    listener()
