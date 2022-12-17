#!/usr/bin/env python
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the dependencies as described in example_pub.py
import rospy
# from std_msgs.msg import String
# from planning.msg import scale_msg
from std_msgs.msg import Float32
# from rosserial_arduino.msg import Adc
import time

global curr_weight

# Define the callback method which is called whenever this node receives a 
# message on its subscribed topic. The received message is passed as the first
# argument to callback().
def callback(message):
    global curr_weight
    curr_weight = message.data

def listener():
    # Create a new instance of the rospy.Subscriber object which we can use to
    # receive messages of type Float32 from the topic /arduino/scalePour.
    # Whenever a new message is received, the method callback() will be called
    # with the received message as its first argument.
    global curr_weight
    rospy.Subscriber("/arduino/scalePour", Float32, callback)
    time.sleep(1)
    print("Ran Arduino subscriber")
    return curr_weight

# Python's syntax for a main() method
if __name__ == '__main__':
    pass

def continue_pour(curr_weight, mass_lim):
    '''
    Makes a Decision based on when to stop pouring based on how much mass is measured on the scale
    '''
    if (curr_weight < mass_lim):
        return True
    else:
        return False
