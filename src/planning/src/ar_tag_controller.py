#!/usr/bin/env python
#The line above tells Linux that this file is a Python script,
#and that the OS should use the Python interpreter in /usr/bin/env
#to run it. Don't forget to use "chmod +x [filename]" to make
#this script executable.

#Import the rospy package. For an import to work, it must be specified
#in both the package manifest AND the Python file in which it is used.
import rospy
import tf2_ros
import sys
import numpy as np

from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from geometry_msgs.msg import TransformStamped

#Define the method which contains the main functionality of the node.
def controller(turtlebot_frame, goal_frame):
  """
  Controls a turtlebot whose position is denoted by turtlebot_frame,
  to go to a position denoted by target_frame
  Inputs:
  - turtlebot_frame: the tf frame of the AR tag on your turtlebot
  - target_frame: the tf frame of the target AR tag
  """

  # Create a publisher and a tf buffer, which is primed with a tf listener
  # pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
  tfBuffer = tf2_ros.Buffer()
  tfListener = tf2_ros.TransformListener(tfBuffer)
  
  # Create a timer object that will sleep long enough to result in
  # a 10Hz publishing rate
  r = rospy.Rate(10) # 10hz

  # Loop until the node is killed with Ctrl-C
  found_cup = False
  # while not rospy.is_shutdown():
  while not found_cup:
    try:
      # print(turtlebot_frame)
      # print(goal_frame)
      trans = tfBuffer.lookup_transform(turtlebot_frame, goal_frame, rospy.Time())
      found_cup = True
      # Process trans to get your state error
      # Generate a control command to send to the robot
      info = trans.transform
      # print(info.translation.x)
      # print(info.translation.y)
      # vector2 = np.array([info.translation.x, info.translation.y]).T
      # print(vector2)
      # control_command = matrix1 @ vector2
      # print(control_command)
      # twist_cmd = Twist()
      # print("info: ", info)
      # print("Translation x: ", info.translation.x)
      # print("Translation y: ", info.translation.y)
      # print("Translation z: ", info.translation.z)
      # print("Rotation x: ", info.rotation.x)
      # print("Rotation y: ", info.rotation.y)
      # print("Rotation z: ", info.rotation.z)
      # print("Rotation w: ", info.rotation.w)

      # twist_cmd.linear.x = K1 * info.translation.x
      # twist_cmd.linear.x = 0
      # twist_cmd.linear.y = K2 * info.translation.y
      # twist_cmd.linear.y = 0
      # twist_cmd.linear.z = 0
      # twist_cmd.angular.x = 0
      # twist_cmd.angular.y = 0
      # twist_cmd.angular.z = K2 * info.translation.y

      # pub.publish(twist_cmd)
      return info
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
      print("Exception thrown ", e)
      pass
    # # Use our rate object to sleep until it is time to publish again
    # r.sleep()

      
# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method

  #Run this program as a new node in the ROS computation graph 
  #called /turtlebot_controller.
  rospy.init_node('ar_tag_controller', anonymous=True)

  try:
    controller(sys.argv[1], sys.argv[2])
  except rospy.ROSInterruptException:
    pass
