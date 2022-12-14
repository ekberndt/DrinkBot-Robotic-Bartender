#!/usr/bin/env python
import numpy as np
import rospy
from planning.srv import enviro  # Service type
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32
# from geometry_msgs.msg import Twist
from planning.srv import grip  # Service type
from intera_interface import gripper as robot_gripper
import ar_tag_controller
import joint_position_angles
from path_planner import PathPlanner
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
    print("ar_tag")
    print(ar_tag)
    print("base")
    print(base)
    ar_tag_in_base_frame.pose.position.x = -(ar_tag.translation.x - base.translation.x) - offset.pose.position.x
    ar_tag_in_base_frame.pose.position.y = -(ar_tag.translation.y - base.translation.y) - offset.pose.position.y
    ar_tag_in_base_frame.pose.position.z = -(ar_tag.translation.z - base.translation.z) - offset.pose.position.z

    ar_tag_in_base_frame.pose.orientation.x = 0.0
    ar_tag_in_base_frame.pose.orientation.y = -1.0
    ar_tag_in_base_frame.pose.orientation.z = 0.0
    ar_tag_in_base_frame.pose.orientation.w = 0.0
    print("ar_tag_in_base_frame")
    print(ar_tag_in_base_frame)

    return ar_tag_in_base_frame

def grip_client(toggle_open_close):
    # Initialize the client node
    # rospy.init_node('grip_client')
    # Wait until patrol service is ready
    # rospy.wait_for_service('/turtle1/patrol')
    # rospy.wait_for_service('/sawyer_parms/grip')
    try:
        # Acquire service proxy
        # grip_proxy = rospy.ServiceProxy(
            # '/sawyer_parms/grip', grip)
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
        


    #     rospy.loginfo('Closing Gripper')
    #     # Call patrol service via the proxy
    #     while not rospy.is_shutdown():
    #         input("press enter to grip")
    #         msg = toggle_open_close
    #         grip_proxy(msg)
    

        right_gripper = robot_gripper.Gripper('right_gripper')

        

        # if (request.grip):
        if(toggle_open_close):
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
    global toggle
    # Initialize the client node
    rospy.init_node('ar_tag_client')
    # Wait until sawyer_params/enviro topic
    print("Wait")
    rospy.wait_for_service('/sawyer_parms/enviro')
    print("Started client")
    try:
        # Acquire service proxy
        sawyer_proxy = rospy.ServiceProxy(
            '/sawyer_parms/enviro', enviro)

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
        # 1 inch = 0.0266 robot units
        offset = PoseStamped()
        offset.header.frame_id = "base"
        offset.pose.position.x = -0.5 * 0.0266
        offset.pose.position.y = 0.5 * 0.0266
        offset.pose.position.z = 5.0 * 0.0266
        offset.pose.orientation.x = 0.0
        offset.pose.orientation.y = 0.0
        offset.pose.orientation.z = 0.0
        offset.pose.orientation.w = 0.0

        ar_marker_base = ar_tag_controller.controller("camera_link", "ar_marker_15") # Base ar_tag
        ar_marker_11 = ar_tag_controller.controller("camera_link", "ar_marker_11") # Blue cup
        ar_marker_14 = ar_tag_controller.controller("camera_link", "ar_marker_14") # Green cup
        ar_marker_11_base = camera_to_base_frame(ar_marker_base, ar_marker_11, offset)
        ar_marker_14_base = camera_to_base_frame(ar_marker_base, ar_marker_14, offset)

        # Create an instance of the rospy.Publisher object which we can  use to
        # publish messages to a topic. This publisher publishes messages of type
        # std_msgs/String to the topic /chatter_talk
        # pub = rospy.Publisher('user_messages', PoseStamped(), queue_size=10)
        
        # Create a timer object that will sleep long enough to result in a 10Hz
        # publishing rate
        # r = rospy.Rate(10) # 10hz
        # rospy.loginfo('Sending ar tag positions')
        # test = PoseStamped()
        # test.pose.position.x = 1
        # test1 = 4
        # print(test)
        # pub.publish(test1)
        # print("Published")

        pos1 = ar_marker_14_base

        pos2 = PoseStamped()
        pos2.header.frame_id = "base"
        pos2.pose.position.x = pos1.pose.position.x
        pos2.pose.position.y = pos1.pose.position.y
        pos2.pose.position.z = pos1.pose.position.z - 5 * 0.0266
        pos2.pose.orientation.x = pos1.pose.orientation.x
        pos2.pose.orientation.y = pos1.pose.orientation.y
        pos2.pose.orientation.z = pos1.pose.orientation.z
        pos2.pose.orientation.w = pos1.pose.orientation.w

        ar_marker_11_base_added_z = PoseStamped()
        ar_marker_11_base_added_z.header.frame_id = "base"
        ar_marker_11_base_added_z.pose.position.x = ar_marker_11_base.pose.position.x
        ar_marker_11_base_added_z.pose.position.y = ar_marker_11_base.pose.position.y + 3 * 0.0266
        ar_marker_11_base_added_z.pose.position.z = ar_marker_11_base.pose.position.z + 13 * 0.0266
        ar_marker_11_base_added_z.pose.orientation.x = ar_marker_11_base.pose.orientation.x
        ar_marker_11_base_added_z.pose.orientation.y = ar_marker_11_base.pose.orientation.y
        ar_marker_11_base_added_z.pose.orientation.z = ar_marker_11_base.pose.orientation.z
        ar_marker_11_base_added_z.pose.orientation.w = ar_marker_11_base.pose.orientation.w

        pos4 = ar_marker_11_base_added_z

        rospy.loginfo('Sending ar tag positions')
        # Call patrol service via the proxy
        positions = 10
        i = 0

        # Calibrate gripper
        right_gripper = robot_gripper.Gripper('right_gripper')
        print('Calibrating...')
        right_gripper.calibrate()
        rospy.sleep(2.0)


        planner = PathPlanner("right_arm")
        curr_state = planner.get_state()
        print(curr_state)
        # while not rospy.is_shutdown():
        while i < positions:
            # input("press enter to move")
            if i == 0:
            # if i == 0:
                goal = pos1
                orient_tf = False
                print(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i== 1:
            # elif
                goal = pos2
                orient_tf = False
                print(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 2:
                grip_client(True)
            #     goal = pos3
            #     orient_tf = False
            elif i == 3:
                print("3")
                pos1.pose.position.z = pos1.pose.position.z + 10 * 0.0266
                goal = pos1
                print(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            elif i == 4:
                print("4")
                goal = pos4
                print(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
                sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            # elif i == 5:
            #     print("5")
            #     orient_tf = True
            #     print(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
            #     sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
                
            elif i == 6:    
                print("6")
                # orient_tf = True
                # print(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
                # sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)
                grip_client(False)
                # planner = PathPlanner("right_arm")
                # curr_state = planner.get_state()
                # print(curr_state)
                # # joint_position_angles.
            toggle += 1
            i += 1



    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)

    # rospy.spin()

# # Define the method which contains the node's main functionality
# def talker():
#     global toggle
#     # Initialize the client node
#     # rospy.init_node('ar_tag_client')
#     # Wait until sawyer_params/enviro topic
#     # rospy.wait_for_service('/sawyer_parms/enviro')
#     print("Start client")
#     # Acquire service proxy
#     sawyer_proxy = rospy.ServiceProxy(
#         '/sawyer_parms/enviro', enviro)

#     # Create an instance of the rospy.Publisher object which we can  use to
#     # publish messages to a topic. This publisher publishes messages of type
#     # std_msgs/String to the topic /chatter_talk
#     pub = rospy.Publisher('user_messages', PoseStamped, queue_size=10)
    
#     # Create a timer object that will sleep long enough to result in a 10Hzoffset = PoseStamped()
#     offset = PoseStamped()
#     offset.header.frame_id = "base"
#     offset.pose.position.x = 4 * 0.0266
#     offset.pose.position.y = 0
#     offset.pose.position.z = 0
#     offset.pose.orientation.x = 0.0
#     offset.pose.orientation.y = -1.0
#     offset.pose.orientation.z = 0.0
#     offset.pose.orientation.w = 0.0

#     # test_pos = PoseStamped()
#     # test_pos.header.frame_id = "base"
#     # test_pos.pose.position.x = 0.5
#     # test_pos.pose.position.y = 0.5
#     # test_pos.pose.position.z = 1
#     # test_pos.pose.orientation.x = 0.0
#     # test_pos.pose.orientation.y = -1.0
#     # test_pos.pose.orientation.z = 0.0
#     # test_pos.pose.orientation.w = 0.0

#     # ar_marker_base = ar_tag_controller.controller("camera_link", "ar_marker_15") # Base ar_tag
#     # # ar_marker_11 = ar_tag_controller.controller("camera_link", "ar_marker_11") # Blue cup
#     # ar_marker_14 = ar_tag_controller.controller("camera_link", "ar_marker_14") # Green cup
#     # # ar_marker_11_base = camera_to_base_frame(ar_marker_base, ar_marker_11, offset)
#     # ar_marker_14_base = camera_to_base_frame(ar_marker_base, ar_marker_14, offset)

#     # rospy.loginfo('Sending ar tag positions')
#     # test = PoseStamped()
#     # pub.publish(ar_marker_14_base)
#     # # pub.publish(test_pos)
#     # rospy.loginfo('Published')
#     # print(rospy.get_name() + ": I sent \"%s\"" % user_string)
#     # publishing rate
#     r = rospy.Rate(10) # 10hz

#     # Loop until the node is killed with Ctrl-C
#     while not rospy.is_shutdown():
#         # Construct a string that we want to publish (in Python, the "%"
#         # operator functions similarly to sprintf in C or MATLAB)
#         # pub_string = "Please enter a line of text and press <Enter>"
#         # print(pub_string)
#         # user_string = input()
#         # time_stamp = rospy.get_time()
#         # item = TimestampString(user_string, time_stamp)
#         # Publish our string to the 'chatter_talk' topic
#         # # Acquire service proxy
#         # sawyer_proxy = rospy.ServiceProxy(
#         #     '/sawyer_parms/enviro', enviro)
#         try:
#             offset = PoseStamped()
#             offset.header.frame_id = "base"
#             offset.pose.position.x = 4 * 0.0266
#             offset.pose.position.y = 0
#             offset.pose.position.z = 0
#             offset.pose.orientation.x = 0.0
#             offset.pose.orientation.y = -1.0
#             offset.pose.orientation.z = 0.0
#             offset.pose.orientation.w = 0.0

#             # test_pos = PoseStamped()
#             # test_pos.header.frame_id = "base"
#             # test_pos.pose.position.x = 0.5
#             # test_pos.pose.position.y = 0.5
#             # test_pos.pose.position.z = 1
#             # test_pos.pose.orientation.x = 0.0
#             # test_pos.pose.orientation.y = -1.0
#             # test_pos.pose.orientation.z = 0.0
#             # test_pos.pose.orientation.w = 0.0

#             ar_marker_base = ar_tag_controller.controller("camera_link", "ar_marker_15") # Base ar_tag
#             # ar_marker_11 = ar_tag_controller.controller("camera_link", "ar_marker_11") # Blue cup
#             ar_marker_14 = ar_tag_controller.controller("camera_link", "ar_marker_14") # Green cup
#             # ar_marker_11_base = camera_to_base_frame(ar_marker_base, ar_marker_11, offset)
#             ar_marker_14_base = camera_to_base_frame(ar_marker_base, ar_marker_14, offset)

#             rospy.loginfo('Sending ar tag positions')
#             # test = PoseStamped()
#             pub.publish(ar_marker_14_base)
#             # pub.publish(test_pos)
#             rospy.loginfo('Published')
#             # print(rospy.get_name() + ": I sent \"%s\"" % user_string)
#         except e:
#             pass
        
        # Use our rate object to sleep until it is time to publish again
        r.sleep()


if __name__ == '__main__':
    # Run this program as a new node in the ROS computation graph called /talker.
    # rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    # try:
    #     talker()
    # except rospy.ROSInterruptException: pass
    sawyer_client()
