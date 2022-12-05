#!/usr/bin/env python
import numpy as np
import rospy
from planning.srv import enviro  # Service type
# from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped
# from geometry_msgs.msg import Twist
import ar_tag_controller
toggle = 0

# def callback(message):
#     # Print the message to the console

def camera_to_base_frame(base, ar_tag, offset):
    """ converts coordinates in the camera frame to coordinates
    in the base frame of the robot

    Parameters
    ----------
    base : PoseStamped
        the frame of the ar tag taped to the base of the robot
    ar_tag : PoseStamped
        the frame of the ar tag
    offset : PoseStamped
        the offset of the taped ar tag (base) to the true robot base frame
    
    Returns
    -------
    ar_tag_in_base_frame
        a PoseStamped representing ar_tag in the base frame
    """
    ar_tag_in_base_frame = PoseStamped()

    ar_tag_in_base_frame.header.frame_id = "base"
    ar_tag_in_base_frame.pose.position.x = ar_tag - base.translation.x - offset
    ar_tag_in_base_frame.pose.position.y = ar_tag - base.translation.y - offset
    ar_tag_in_base_frame.pose.position.z = ar_tag - base.translation.z - offset

    ar_tag_in_base_frame.pose.orientation.x = 0.0
    ar_tag_in_base_frame.pose.orientation.y = -1.0
    ar_tag_in_base_frame.pose.orientation.z = 0.0
    ar_tag_in_base_frame.pose.orientation.w = 0.0

    return ar_tag_in_base_frame

def sawyer_client():
    global toggle
    # Initialize the client node
    rospy.init_node('ar_tag_client')
    # Wait until sawyer_params/enviro topic
    rospy.wait_for_service('/sawyer_parms/enviro')
    try:
        # Acquire service proxy
        sawyer_proxy = rospy.ServiceProxy(
            '/sawyer_parms/enviro', enviro)


        # vel = 2.0  # Linear velocity
        # omega = 1.0  # Angular velocity

        #Test Case 1 Obstacle
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
        # goal.pose.position.x = 0.502
        # goal.pose.position.y = -0.394
        # goal.pose.position.z = -0.133

        #Orientation as a quaternion
        # goal.pose.orientation.x = 0.0
        # goal.pose.orientation.y = -1.0
        # goal.pose.orientation.z = 0.0
        # goal.pose.orientation.w = 0.0

        
        # Call ar_tag_controller to get translation from camera frame to a given ar tag
        ar_marker_1 = ar_tag_controller.controller("base_link", "ar_marker_1")

        # #pos1
        # pos1 = PoseStamped()
        # pos1.header.frame_id = "base"
        # pos1.pose.position.x = 0.603
        # pos1.pose.position.y = 0.273
        # pos1.pose.position.z = 0.046

        # pos1.pose.orientation.x = 0.0
        # pos1.pose.orientation.y = -1.0
        # pos1.pose.orientation.z = 0.0
        # pos1.pose.orientation.w = 0.0

        # #pos2
        # pos2 = PoseStamped()
        # pos2.header.frame_id = "base"
        # pos2.pose.position.x = 0.603
        # pos2.pose.position.y = 0.273
        # pos2.pose.position.z = -0.120

        # pos2.pose.orientation.x = 0.0
        # pos2.pose.orientation.y = -1.0
        # pos2.pose.orientation.z = 0.0
        # pos2.pose.orientation.w = 0.0
        
        rospy.loginfo('Sending ar tag positions')
        # Call patrol service via the proxy
        positions = 1
        i = 0
        # while not rospy.is_shutdown():
        while i < positions:
            # input("press enter to move")
            if toggle % positions == 0:
            # if i == 0:
                goal = pos1
                orient_tf = False
            elif toggle % positions == 1:
            # elif
                goal = pos2
                orient_tf = True
            else:
                goal = pos3
                orient_tf = True
            toggle += 1

            sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)

    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)


if __name__ == '__main__':
    sawyer_client()

