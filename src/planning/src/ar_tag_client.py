#!/usr/bin/env python
import numpy as np
import rospy
from planning.srv import enviro  # Service type
from planning.srv import forward_kinematics # Service type
from std_srvs.srv import Empty, SetBool # Empty service type
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32
# from geometry_msgs.msg import Twist
from planning.srv import grip  # Service type
from intera_interface import gripper as robot_gripper
import ar_tag_controller
import forward_kinematics_server
from path_planner import PathPlanner
import scale_sub
import time
import os

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
    print("ar_tag")
    print(ar_tag)
    print("base")
    print(base)
    ar_tag_in_base_frame.pose.position.x = -(ar_tag.translation.x - base.translation.x) + offset.pose.position.x
    ar_tag_in_base_frame.pose.position.y = -(ar_tag.translation.y - base.translation.y) + offset.pose.position.y
    ar_tag_in_base_frame.pose.position.z = -(ar_tag.translation.z - base.translation.z) + offset.pose.position.z

    ar_tag_in_base_frame.pose.orientation.x = 0.0
    ar_tag_in_base_frame.pose.orientation.y = -1.0
    ar_tag_in_base_frame.pose.orientation.z = 0.0
    ar_tag_in_base_frame.pose.orientation.w = 0.0
    print("ar_tag_in_base_frame")
    print(ar_tag_in_base_frame)

    return ar_tag_in_base_frame

def grip_client(gripper_close):
    # Initialize the client node
    try:
        global right_gripper
        if(gripper_close):
            # Close the right gripper
            print('Closing...')
            right_gripper.close()
            print('I should have closed')
            rospy.sleep(1.0)
            print('I made to after sleep')
        else:
            # Open the right gripper
            print('Opening...')
            right_gripper.open()
            rospy.sleep(1.0)
            print('Done!')
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)

def sawyer_client():
    # Initialize the client node
    rospy.init_node('ar_tag_client')
    # Wait until sawyer_params/enviro topic
    print("Waiting for Sawyer Server")
    rospy.wait_for_service('/sawyer_parms/enviro')
    print("Started client")
    try:
        # Acquire service proxy for Sawyer Server
        sawyer_proxy = rospy.ServiceProxy(
            '/sawyer_parms/enviro', enviro)

        forward_kinematic_proxy = rospy.ServiceProxy(
            '/forward_kinematics_positions', forward_kinematics)

        #Test Case 1 Obstacle
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
        
        # Call ar_tag_controller to get translation from camera frame to a given ar tag
        # 1 inch = 0.0266 robot units
        offset = PoseStamped()
        offset.header.frame_id = "base"
        offset.pose.position.x = 3 * 0.0266
        offset.pose.position.y = 5.2 * 0.0266
        offset.pose.position.z = -5.5 * 0.0266
        offset.pose.orientation.x = 0.0
        offset.pose.orientation.y = 0.0
        offset.pose.orientation.z = 0.0
        offset.pose.orientation.w = 0.0

        ar_marker_base = ar_tag_controller.controller("camera_link", "ar_marker_15") # Base ar_tag
        ar_marker_11 = ar_tag_controller.controller("camera_link", "ar_marker_11") # Blue cup
        ar_marker_14 = ar_tag_controller.controller("camera_link", "ar_marker_14") # Green cup
        ar_marker_17 = ar_tag_controller.controller("camera_link", "ar_marker_17") # Product cup
        ar_marker_11_base = camera_to_base_frame(ar_marker_base, ar_marker_11, offset)
        ar_marker_14_base = camera_to_base_frame(ar_marker_base, ar_marker_14, offset)
        ar_marker_17_base = camera_to_base_frame(ar_marker_base, ar_marker_17, offset)

        # Position above green cup
        pos1 = ar_marker_14_base

        # Position with grippers around green cup
        pos2 = PoseStamped()
        pos2.header.frame_id = "base"
        pos2.pose.position.x = pos1.pose.position.x
        pos2.pose.position.y = pos1.pose.position.y
        pos2.pose.position.z = pos1.pose.position.z - 3 * 0.0266
        pos2.pose.orientation.x = pos1.pose.orientation.x
        pos2.pose.orientation.y = pos1.pose.orientation.y
        pos2.pose.orientation.z = pos1.pose.orientation.z
        pos2.pose.orientation.w = pos1.pose.orientation.w

        # Position above blue cup
        pos5 = ar_marker_11_base

        # Position with grippers around blue cup
        pos6 = PoseStamped()
        pos6.header.frame_id = "base"
        pos6.pose.position.x = pos5.pose.position.x
        pos6.pose.position.y = pos5.pose.position.y
        pos6.pose.position.z = pos5.pose.position.z - 3 * 0.0266
        pos6.pose.orientation.x = pos5.pose.orientation.x
        pos6.pose.orientation.y = pos5.pose.orientation.y
        pos6.pose.orientation.z = pos5.pose.orientation.z
        pos6.pose.orientation.w = pos5.pose.orientation.w

        # Position above product cup
        ar_marker_17_base_added_xz = PoseStamped()
        ar_marker_17_base_added_xz.header.frame_id = "base"
        ar_marker_17_base_added_xz.pose.position.x = ar_marker_17_base.pose.position.x + -12 * 0.0266
        ar_marker_17_base_added_xz.pose.position.y = ar_marker_17_base.pose.position.y + 0 * 0.0266
        ar_marker_17_base_added_xz.pose.position.z = ar_marker_17_base.pose.position.z + 2 * 0.0266
        ar_marker_17_base_added_xz.pose.orientation.x = ar_marker_17_base.pose.orientation.x
        ar_marker_17_base_added_xz.pose.orientation.y = ar_marker_17_base.pose.orientation.y
        ar_marker_17_base_added_xz.pose.orientation.z = ar_marker_17_base.pose.orientation.z
        ar_marker_17_base_added_xz.pose.orientation.w = ar_marker_17_base.pose.orientation.w        
        pos4 = ar_marker_17_base_added_xz

        rospy.loginfo('Sending ar tag positions')
        # Call patrol service via the proxy
        positions = 16
        i = 0

        # Calibrate gripper
        global right_gripper
        right_gripper = robot_gripper.Gripper('right_gripper')
        print('Calibrating...')
        right_gripper.calibrate()
        rospy.sleep(2.0)

        planner = PathPlanner("right_arm")
        curr_state = planner.get_state()
        print(curr_state)
        while i < positions:
            if i == 0:
                goal = pos1
                orient_tf = False
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i== 1:
                goal = pos2
                orient_tf = False
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 2:
                # Open then close the gripper
                # Gripper must be opened before it can be closed
                grip_client(False)
                grip_client(True)
            elif i == 3:
                print("3")
                print("Moving to Sawyer Tuck position")
                os.system("roslaunch planning sawyer_tuck.launch")
            elif i == 4:
                print("Moving to above product cup")
                goal = pos4
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 5:
                forward_kinematic_proxy(False, 0)
                print("Forward Proxy Completed")

                # Jitter cup until desired weight is reached
                global curr_weight
                curr_weight = 0
                curr_weight = scale_sub.listener()
                mass_lim = 5
                continue_pour_check = scale_sub.continue_pour(curr_weight, mass_lim)
                j = 0
                while(continue_pour_check):
                    print("Continuing to pour with weight: " + str(curr_weight))
                    forward_kinematic_proxy(True, j)
                    curr_weight = scale_sub.listener()
                    time.sleep(1)
                    continue_pour_check = scale_sub.continue_pour(curr_weight, mass_lim)            
                    j += 1
                    time.sleep(3)
            elif i == 6:    
                print("6")
                goal = pos2
                orient_tf = False
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 7:
                print('7')
                grip_client(False)
                print("Moving to Sawyer Tuck position")
                os.system("roslaunch planning sawyer_tuck.launch")
            elif i == 8:
                goal = pos5
                orient_tf = False
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i== 9:
                goal = pos6
                orient_tf = False
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 10:
                # Open then close the gripper
                # Gripper must be opened before it can be closed
                grip_client(False)
                grip_client(True)
            elif i == 11:
                print("3")
                print("Moving to Sawyer Tuck position")
                os.system("roslaunch planning sawyer_tuck.launch")
            elif i == 12:
                print("Moving to above product cup")
                goal = pos4
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 13:
                forward_kinematic_proxy(False, 0)
                print("Forward Proxy Completed")

                # Jitter cup until desired weight is reached
                curr_weight = 0
                curr_weight = scale_sub.listener()
                mass_lim = mass_lim + 15
                continue_pour_check = scale_sub.continue_pour(curr_weight, mass_lim)
                j = 0
                while(continue_pour_check):
                    print("Continuing to pour with weight: " + str(curr_weight))
                    forward_kinematic_proxy(True, j)
                    curr_weight = scale_sub.listener()
                    time.sleep(1)
                    continue_pour_check = scale_sub.continue_pour(curr_weight, mass_lim)          
                    j += 1
                    time.sleep(3)
            elif i == 14:    
                print("6")
                goal = pos6
                orient_tf = False
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 15:
                print('7')
                grip_client(False)
                print("Moving to Sawyer Tuck position")
                os.system("roslaunch planning sawyer_tuck.launch")
            i += 1

    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)

if __name__ == '__main__':
    sawyer_client()

