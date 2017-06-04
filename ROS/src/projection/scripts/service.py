#!/usr/bin/env python

from projection.srv import *
import rospy
import sys
sys.path.insert(0, "home/henry/Documents/Projet_Dep_Info/src/projection/nodes")
print(sys.path)
#import position_force_test

def handle_node_manager(req):
    l = req.L
    print(l)
    if len(l) != 0:
        for i in range(0,len(l)):
            print ("Launching node " + str(l[i]))
            position_force_test.myNode(l[i])

def nodes_manager_server():
    rospy.init_node('nodes_manager')
    s = rospy.Service('nodes_manager', service, handle_node_manager)
    print "Ready to manage nodes!!! :D"
    rospy.spin()

if __name__ == "__main__":
    nodes_manager_server()
