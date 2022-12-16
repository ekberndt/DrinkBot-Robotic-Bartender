#!/usr/bin/env python
import numpy as np
import rospy
# from turtle_patrol.srv import Patrol  # Import service type
from planning.srv import grip  # Service type
# from turtlesim.srv import TeleportAbsolute
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped

def grip_client():
    # Initialize the client node
    rospy.init_node('grip_client')
    # Wait until patrol service is ready
    # rospy.wait_for_service('/turtle1/patrol')
    rospy.wait_for_service('/sawyer_parms/grip')
    try:
        # Acquire service proxy
        grip_proxy = rospy.ServiceProxy(
            '/sawyer_parms/grip', grip)
        # vel = 2.0  # Linear velocity
        # omega = 1.0  # Angular velocity

        #Test Case 1
        msg = False

        # obj_posx = np.array([2])
        # obj_posy = np.array([2])
        # obj_posz = np.array([2])
        # obj_orientx = np.array([0.5])
        # obj_orienty = np.array([0])
        # obj_orientz = np.array([0])
        # obj_orientw = np.array([0])
        # sizex = np.array([0.5])
        # sizey = np.array([0.5])
        # sizez = np.array([0.5])
        # name_obj = np.array(["Brick"])

        # goal = PoseStamped()
        # goal.pose.position.x = 0
        # goal.pose.position.y = 0
        # goal.pose.position.z = 0

        # #Orientation as a quaternion
        # goal.pose.orientation.x = 0.0
        # goal.pose.orientation.y = -1.0
        # goal.pose.orientation.z = 0.0
        # goal.pose.orientation.w = 0.0
        


        rospy.loginfo('Closing Gripper')
        # Call patrol service via the proxy
        while not rospy.is_shutdown():
            input("press enter to grip")
            msg = not msg
            grip_proxy(msg)
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)


if __name__ == '__main__':
    grip_client()

