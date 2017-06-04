#!/usr/bin/env python
import roslib
roslib.load_manifest('projection')
import rospy
from geometry_msgs.msg import WrenchStamped

def callback(data):
    print("hello")
    print(data.wrench.force.x)
    
def subscriber():
    rospy.init_node('subscriber')

    rospy.Subscriber("optoforce_1", WrenchStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    
    rate = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    subscriber()
