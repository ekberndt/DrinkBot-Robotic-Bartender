#!/usr/bin/env python
import numpy as np
import rospy
# from turtle_patrol.srv import Patrol  # Import service type
from planning.srv import enviro  # Service type
# from turtlesim.srv import TeleportAbsolute
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped
# from path_planner import get_current_poses
toggle = 0
def sawyer_client():
    global toggle
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

        # goal = PoseStamped()
        # goal.pose.position.x = 0.502
        # goal.pose.position.y = -0.394
        # goal.pose.position.z = -0.133

        #Orientation as a quaternion
        # goal.pose.orientation.x = 0.0
        # goal.pose.orientation.y = -1.0
        # goal.pose.orientation.z = 0.0
        # goal.pose.orientation.w = 0.0

        

        #pos1
        pos1 = PoseStamped()
        # pos1.header.frame_id = "right_gripper_tip"
        # pos1.pose.position.x = 0.6
        # pos1.pose.position.y = -0.3
        # pos1.pose.position.z = 0.0

        # pos1.pose.orientation.x = -0.789
        # pos1.pose.orientation.y = 0.131
        # pos1.pose.orientation.z = -0.137
        # pos1.pose.orientation.w = 0.584
        pos1.header.frame_id = "base"
        pos1.pose.position.x = 0.603
        pos1.pose.position.y = 0.273
        pos1.pose.position.z = -0.050

        pos1.pose.orientation.x = 0.0
        pos1.pose.orientation.y = -1.0
        pos1.pose.orientation.z = 0.0
        pos1.pose.orientation.w = 0.0
        # pos1.header.frame_id = "base" 
        # pos1.pose.position.x = 0.815
        # pos1.pose.position.y = 0.215
        # pos1.pose.position.z = 0.202

        # pos1.pose.orientation.x = 0.0
        # pos1.pose.orientation.y = -1.0
        # pos1.pose.orientation.z = 0.0
        # pos1.pose.orientation.w = 0.0 

        #pos2
        pos2 = PoseStamped()
        pos2.header.frame_id = "base"
        pos2.pose.position.x = 0.603
        pos2.pose.position.y = 0.273
        pos2.pose.position.z = -0.15

        pos2.pose.orientation.x = 0.0
        pos2.pose.orientation.y = -1.0
        pos2.pose.orientation.z = 0.0
        pos2.pose.orientation.w = 0.0
        # pos2.header.frame_id = "base"
        # pos2.pose.position.x = 0.803
        # pos2.pose.position.y = 0.273
        # pos2.pose.position.z = 0.046

        # pos2.pose.orientation.x = 0.0
        # pos2.pose.orientation.y = 1.0
        # pos2.pose.orientation.z = 0.0
        # pos2.pose.orientation.w = 0.0

        #pos2_5
        pos2_5 = PoseStamped()
        pos2_5.header.frame_id = "base"
        pos2_5.pose.position.x = 0.603
        pos2_5.pose.position.y = 0.273
        pos2_5.pose.position.z = 0.000

        pos2_5.pose.orientation.x = 0.0
        pos2_5.pose.orientation.y = -1.0
        pos2_5.pose.orientation.z = 0.0
        pos2_5.pose.orientation.w = 0.0

        #pos3
        # pos3 = PoseStamped()
        # pos3.header.frame_id = "base"
        # pos3.pose.position.x = 0.665
        # pos3.pose.position.y = -0.214
        # pos3.pose.position.z = -0.120

        # pos3.pose.orientation.x = 0.0
        # pos3.pose.orientation.y = -1.0
        # pos3.pose.orientation.z = 0.0
        # pos3.pose.orientation.w = 0.0
        pos3 = PoseStamped()
        pos3.header.frame_id = "base"
        pos3.pose.position.x = 0.672
        pos3.pose.position.y = -0.142
        pos3.pose.position.z = 0.050

        pos3.pose.orientation.x = 0.0
        pos3.pose.orientation.y = -1.0
        pos3.pose.orientation.z = 0.0
        pos3.pose.orientation.w = 0.0

        # pos3.pose.orientation.x = 0.656
        # pos3.pose.orientation.y = 0.753
        # pos3.pose.orientation.z = 0.002
        # pos3.pose.orientation.w = 0.05
        # pos3.header.frame_id = "base"
        # pos3.pose.position.x = 0.855
        # pos3.pose.position.y = -0.044
        # pos3.pose.position.z = -0.017

        # pos3.pose.orientation.x = 0.0
        # pos3.pose.orientation.y = 1.0
        # pos3.pose.orientation.z = 0.0
        # pos3.pose.orientation.w = 0.0

        #pos4
        pos4 = PoseStamped()
        pos4.header.frame_id = "base"
        pos4.pose.position.x = 0.721
        pos4.pose.position.y = -0.218
        pos4.pose.position.z = 0.357 / 2

        pos4.pose.orientation.x = 0.0
        pos4.pose.orientation.y = 0.0
        pos4.pose.orientation.z = 1.0
        pos4.pose.orientation.w = 0.0
        


        rospy.loginfo('Moving Arm')
        # Call patrol service via the proxy
        positions = 5

        #toggle through different positions using modulus switch case
        while not rospy.is_shutdown():
       
            input("press enter to move")
            if toggle % positions == 0:
                goal = pos1
                orient_tf = False
            elif toggle % positions == 1:
                goal = pos2
                orient_tf = False
            elif toggle % positions == 2:
                goal = pos2_5
                orient_tf = False
            elif toggle % positions == 3:
                goal = pos3
                orient_tf = False
            else:
                goal = pos4
                orient_tf = False
            toggle += 1

            sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)

    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)


if __name__ == '__main__':
    sawyer_client()

