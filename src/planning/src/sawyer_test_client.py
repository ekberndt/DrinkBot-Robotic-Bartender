#!/usr/bin/env python
import numpy as np
import rospy
# from turtle_patrol.srv import Patrol  # Import service type
from planning.srv import enviro  # Service type
# from turtlesim.srv import TeleportAbsolute
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped

def patrol_client():
    # Initialize the client node
    rospy.init_node('sawyer_client')
    # Wait until patrol service is ready
    # rospy.wait_for_service('/turtle1/patrol')
    rospy.wait_for_service('/sawyer_parms/enviro')
    try:
        # Acquire service proxy
        sawyer_proxy = rospy.ServiceProxy(
            '/sawyer_parms/enviro', enviro)
        # vel = 2.0  # Linear velocity
        # omega = 1.0  # Angular velocity

        #Test Case 1


        obj_posx = np.array([2])
        obj_posy = np.array([2])
        obj_posz = np.array([2])
        obj_orientx = np.array([0.5])
        obj_orienty = np.array([0])
        obj_orientz = np.array([0])
        obj_orientw = np.array([0])
        sizex = np.array([0.5])
        sizey = np.array([0.5])
        sizez = np.array([0.5])
        name_obj = np.array(["Brick"])

        goal = PoseStamped()
        goal.pose.position.x = 0
        goal.pose.position.y = 0
        goal.pose.position.z = 0

        #Orientation as a quaternion
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = -1.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 0.0
        


        rospy.loginfo('Moving Arm')
        # Call patrol service via the proxy
        sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, goal)
    except rospy.ServiceException as e:
        rospy.loginfo(e)


if __name__ == '__main__':
    patrol_client()

