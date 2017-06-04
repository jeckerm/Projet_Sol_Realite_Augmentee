#!/usr/bin/env python
import roslib
roslib.load_manifest('projection')
import rospy
from geometry_msgs.msg import WrenchStamped
import std_msgs.msg

def callback(data):
    print("hello")
    print(data.wrench.force.x)
    print(data.header.stamp)
    
def subscriber():
    rospy.init_node('subscriber')

    rospy.Subscriber("optoforce_1", WrenchStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    
    rate = rospy.Rate(1.0)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
