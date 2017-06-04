#!/usr/bin/env python

import sys
import rospy
from projection.srv import *

def manage_nodes_client(L):
    rospy.wait_for_service('nodes_manager')
    try:
       manage_nodes = rospy.ServiceProxy('nodes_manager', service)
       manage_nodes(L)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    print("Execution usage()")
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("ok1")
        L = list(sys.argv[1])
        print "Requesting"
        manage_nodes_client(L)
    else:
        print usage()
        print("stop")
        sys.exit(1)
