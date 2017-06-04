#!/usr/bin/env python

import roslib
roslib.load_manifest('projection')
import rospy
import math
import tf
import geometry_msgs.msg
import tests_affichages
from geometry_msgs.msg import WrenchStamped

class myNode:
    def __init__(self, number):
        rospy.init_node('listener_tf_'+str(number))
        self.subscribe_name = "optoforce_"+str(number)
        self.listener_tf = tf.TransformListener()
        print(self.subscribe_name + " se lance")
        rospy.Subscriber(self.subscribe_name, WrenchStamped, callback = lambda data: self.callback_name(data))
        print(self.subscribe_name + " a souscrit")
        rate = rospy.Rate(1.0)
        rospy.spin()
        

    def callback_name(self,data):

        last_force = data.wrench.force.x
        time = data.header.stamp
        try:
            if self.listener_tf.frameExists('/'+self.subscribe_name):
                print(self.subscribe_name+" existe")
                t = self.listener_tf.getLatestCommonTime("/"+self.subscribe_name, "/world")
                (trans,rot) = self.listener_tf.lookupTransform(self.subscribe_name, '/world', t) #le temps de ce noeud bug ac le ros bag...
                #print("Position")
                #x =tests_affichages.fois_dix(trans[0])
                #print(trans[0],x)
                print(self.subscribe_name+" Force")
                print(last_force)
                print(self.subscribe_name+" Position")
                print(trans[0])
                print(self.subscribe_name+" Time")
                print(time)
                
            else:
                print("NotExist")
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("Exception")
