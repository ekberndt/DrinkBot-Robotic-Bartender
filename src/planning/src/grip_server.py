#!/usr/bin/env python
# import rospy

# from intera_interface import gripper as robot_gripper

# rospy.init_node('gripper_test')


# Calibrate the gripper (other commands won't work unless you do this first)
# print('Calibrating...')
# right_gripper.calibrate()
# rospy.sleep(2.0)

# # Close the right gripper
# print('Closing...')
# right_gripper.close()
# rospy.sleep(1.0)

# # Open the right gripper
# print('Opening...')
# right_gripper.open()
# rospy.sleep(1.0)
# print('Done!')

#!/usr/bin/env python
from geometry_msgs.msg import Twist
import numpy as np
import rospy
from std_srvs.srv import Empty
import sys
from planning.srv import grip  # Service type
# from turtlesim.srv import TeleportAbsolute
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped
from path_planner import PathPlanner
from intera_interface import gripper as robot_gripper

name = ""
def grip_callback(request):
    rospy.loginfo("Got message request")
    # list_obj = []
    # end_goal = request.goal

    # for i in range(len(request.name_obj)):

    #     size = np.array([request.sizex[i], request.sizey[i], request.sizez[i]])
    #     name = request.name_obj
    #     pos = PoseStamped()
    #     pos.header.frame_id = "base"
    #     pos.pose.position.x = request.obj_posx[i]
    #     pos.pose.position.y = request.obj_posy[i]
    #     pos.pose.position.z = request.obj_posz[i]
    #     pos.pose.orientation.x = request.obj_orientx[i]
    #     pos.pose.orientation.y = request.obj_orienty[i]
    #     pos.pose.orientation.z = request.obj_orientz[i]
    #     pos.pose.orientation.w = request.obj_orientw[i]
    #     # plan = planner.plan_to_pose(pos, [])

    #     list_obj.append((size, name, pos))
    # main(list_obj, end_goal)
    # Set up the right gripper
    right_gripper = robot_gripper.Gripper('right_gripper')

    if (request.grip):
    	print('Calibrating...')
    	right_gripper.calibrate()
    	rospy.sleep(2.0)

    	# Close the right gripper
    	print('Closing...')
    	right_gripper.close()
    	rospy.sleep(1.0)
    else:
    	# Open the right gripper
    	print('Opening...')
    	right_gripper.open()
    	rospy.sleep(1.0)
    	print('Done!')



    # clear_proxy()
    # while not rospy.is_shutdown():
    #     pub.publish(cmd)  # Publish to cmd_vel
    #     rate.sleep()  # Sleep until 

    return "gripped firmly"  # This line will never be reached

def grip_server():
    rospy.init_node("grip_server")
    # Register service
    s = rospy.Service(
        "/sawyer_parms/grip",  # Service name
        grip,  # Service type
        grip_callback  # Service callback
    )
    rospy.loginfo('Running grip server...')
    rospy.spin() # Spin the node until Ctrl-C


if __name__ == '__main__':

    grip_server()


