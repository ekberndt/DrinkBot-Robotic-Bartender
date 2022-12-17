#!/usr/bin/env python
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the dependencies as described in example_pub.py
import rospy
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
    joint_states_list = message.position
    try:
        joint_states_dict["right_j0"] = joint_states_list[1]
        joint_states_dict["right_j1"] = joint_states_list[2]
        joint_states_dict["right_j2"] = joint_states_list[3]
        joint_states_dict["right_j3"] = joint_states_list[4]
        joint_states_dict["right_j4"] = joint_states_list[5]
        joint_states_dict["right_j5"] = joint_states_list[6]
        joint_states_dict["right_j6"] = joint_states_list[7]
    except:
        pass

# Define the method which contains the node's main functionality
def listener():

    # Create a new instance of the rospy. Subscriber object which we can use to
    # receive messages of type JointState from the topic /robot/joint_states.
    # Whenever a new message is received, the method callback() will be called
    # with the received message as its first argument.
    rospy.Subscriber("robot/joint_states", JointState, callback)
    print("listener")

def get_joint_states():
    global joint_states_dict
    listener()

    while(joint_states_dict["right_j0"] == None):
        print("Failed")
        time.sleep(1)
    return joint_states_dict

# Python's syntax for a main() method
if __name__ == '__main__':
    pass