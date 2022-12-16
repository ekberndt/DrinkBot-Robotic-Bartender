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

global message_to_return

def sawyer_client(ar_tag):
    global toggle
    # Initialize the client node
    rospy.wait_for_service('/sawyer_parms/enviro')
    try:
        # Acquire service proxy
        sawyer_proxy = rospy.ServiceProxy(
            '/sawyer_parms/enviro', enviro)

        #Test Case 1 - Creates a random object
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


        # CREATED A SET OF POSITIONS TO CYCLE THROUGH WHEN TESTING SAWYER_SERVER.PY---------------------------
        
        # pos1 = PoseStamped()
        pos1 = ar_tag

        # # pos1.header.frame_id = "right_gripper_tip"
        # # pos1.pose.position.x = 0.6
        # # pos1.pose.position.y = -0.3
        # # pos1.pose.position.z = 0.0

        # # pos1.pose.orientation.x = -0.789
        # # pos1.pose.orientation.y = 0.131
        # # pos1.pose.orientation.z = -0.137
        # # pos1.pose.orientation.w = 0.584
        # pos1.header.frame_id = "base"
        # pos1.pose.position.x = 0.603
        # pos1.pose.position.y = 0.273
        # pos1.pose.position.z = -0.050

        # pos1.pose.orientation.x = 0.0
        # pos1.pose.orientation.y = -1.0
        # pos1.pose.orientation.z = 0.0
        # pos1.pose.orientation.w = 0.0


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
        
        #--------------------------------------------------------------------------------------

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

            print("sawyer_proxy")
            sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, orient_tf, goal)

    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)

# Define the callback method which is called whenever this node receives a 
# message on its subscribed topic. The received message is passed as the first
# argument to callback().
def callback(message):

    # Print the contents of the message to the console

    # print("Message: " + message + ", Received at: " + str(rospy.get_time()))
    print("callback", message)
    message_to_return = message
    sawyer_client(message_to_return)

# Define the method which contains the node's main functionality
def listener():

    # Create a new instance of the rospy.Subscriber object which we can use to
    # receive messages of type std_msgs/String from the topic /chatter_talk.
    # Whenever a new message is received, the method callback() will be called
    # with the received message as its first argument.
    rospy.Subscriber("user_messages", PoseStamped, callback)

    # Wait for messages to arrive on the subscribed topics, and exit the node
    # when it is killed with Ctrl+C
    # try:
    #     print(message_to_return)
    # except e:
    #     print(e)
    rospy.spin()

    # return coordinates

if __name__ == '__main__':
    # Run this program as a new node in the ROS computation graph called
    # /listener_<id>, where <id> is a randomly generated numeric string. This
    # randomly generated name means we can start multiple copies of this node
    # without having multiple nodes with the same name, which ROS doesn't allow.
    # rospy.init_node('listener', anonymous=True)
    rospy.init_node('sawyer_client')
    listener()
    # print(message_to_return)
    

