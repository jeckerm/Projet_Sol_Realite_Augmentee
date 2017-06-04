#!/usr/bin/env python

import roslib
roslib.load_manifest('projection')
import rospy
import math
import tf
import geometry_msgs.msg
import tests_affichages
from geometry_msgs.msg import WrenchStamped


def callback_nom(data,nom):
    last_force = data.wrench.force.x
    time = data.header.stamp
    try:
        if listener_tf.frameExists('/'+nom):
            print(nom+" existe")
            t = listener_tf.getLatestCommonTime("/"+nom, "/world")
            (trans,rot) = listener_tf.lookupTransform(nom, '/world', time) #le temps de ce noeud bug ac le ros bag...
            #print("Position")
            #x =tests_affichages.fois_dix(trans[0])
            #print(trans[0],x)
            print(nom+" Force")
            print(last_force)
            print(nom+" Position")
            print(trans[0])
            print(nom+" Time")
            print(time)
            
        else:
            print("NotExist")
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        print("Exception")



def listener():
    rospy.init_node('listener_tf')
    nom = "optoforce_1"
    print(nom + " se lance")
    global listener_tf
    listener_tf = tf.TransformListener()
    rospy.Subscriber(nom, WrenchStamped, callback = lambda data: callback_nom(data,nom))
    print("J'ai souscrit")
    rate = rospy.Rate(1.0)
    rospy.spin()
    
if __name__ == '__main__':
    listener()
