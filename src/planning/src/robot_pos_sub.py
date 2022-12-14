#!/usr/bin/env python
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the dependencies as described in example_pub.py
import rospy
# from std_msgs.msg import String
# from my_chatter.msg import TimestampString
from sensor_msgs.msg import JointState
import time

joint_states_dict = {
    "right_j0": None,
    "right_j1": None,
    "right_j2": None,
    "right_j3": None,
    "right_j4": None,
    "right_j5": None,
    "right_j6": None
}

# Define the callback method which is called whenever this node receives a 
# message on its subscribed topic. The received message is passed as the first
# argument to callback().
def callback(message):
    global joint_states_dict
    # Print the contents of the message to the console
    # print("Joint States:\n" + str(message)) #+ "\nSent at: " + str(message.timestamp) + "\nReceived at: " + str(rospy.get_time()))
    joint_states_list = message.position
    # print(joint_states_list)
    try:
        joint_states_dict["right_j0"] = joint_states_list[1]
        joint_states_dict["right_j1"] = joint_states_list[2]
        joint_states_dict["right_j2"] = joint_states_list[3]
        joint_states_dict["right_j3"] = joint_states_list[4]
        joint_states_dict["right_j4"] = joint_states_list[5]
        joint_states_dict["right_j5"] = joint_states_list[6]
        joint_states_dict["right_j6"] = joint_states_list[7]
        # print("Assigned joint states to dictionary")
        # print(joint_states_dict)
    except:
        # print("Failed to assign joint states to dictionary")
        # rospy.sleep(2)
        # listener()
        pass

# Define the method which contains the node's main functionality
def listener():

    # Create a new instance of the rospy. Subscriber object which we can use to
    # receive messages of type std_msgs/String from the topic /robot/joint_states.
    # Whenever a new message is received, the method callback() will be called
    # with the received message as its first argument.
    rospy.Subscriber("robot/joint_states", JointState, callback)
    print("listener")

def get_joint_states():
    global joint_states_dict
    # rospy.init_node('listener', anonymous=True)
    listener()

    while(joint_states_dict["right_j0"] == None):
        print("Failed")
        time.sleep(1)
    # def shutdown_statement()
    #     print("Shutting down subscriber node")

    # rospy.signal_shutdown("Shutting down subscriber node")
    return joint_states_dict

# Python's syntax for a main() method
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called
    # /listener_<id>, where <id> is a randomly generated numeric string. This
    # randomly generated name means we can start multiple copies of this node
    # without having multiple nodes with the same name, which ROS doesn't allow.
    # rospy.init_node('listener', anonymous=True)

    # listener()
    print("Main")
    pass