#!/usr/bin/env python
from geometry_msgs.msg import Twist
import numpy as np
import rospy
from std_srvs.srv import Empty # Service type
import sys
from planning.srv import enviro # Service type
from planning.srv import forward_kinematics # Service type
from path_test import main #Link to Arm Movement
from moveit_msgs.msg import OrientationConstraint, PositionConstraint
from geometry_msgs.msg import PoseStamped
from path_planner import PathPlanner

name = ""
def sawyer_callback(request):
    # Clear historical path traces
    rospy.loginfo("Got message request")
    list_obj = []
    end_goal = request.goal
    print(request)
    
    # Fills rviz with as many objects as inputted from 
    # the client node
    for i in range(len(request.name_obj)):
        size = np.array([request.sizex[i], request.sizey[i], request.sizez[i]])
        name = request.name_obj
        pos = PoseStamped()
        pos.header.frame_id = "base"
        pos.pose.position.x = request.obj_posx[i]
        pos.pose.position.y = request.obj_posy[i]
        pos.pose.position.z = request.obj_posz[i]
        pos.pose.orientation.x = request.obj_orientx[i]
        pos.pose.orientation.y = request.obj_orienty[i]
        pos.pose.orientation.z = request.obj_orientz[i]
        pos.pose.orientation.w = request.obj_orientw[i]
        # plan = planner.plan_to_pose(pos, [])

        list_obj.append((size, name, pos))


   
    # Orientation Block #
    #--------------------------#
    orien_const = OrientationConstraint()
    orien_const.link_name = "right_gripper_tip";
    orien_const.header.frame_id = "base";
    orien_const.orientation
    orien_const.orientation.x = 0.0
    orien_const.orientation.y = -1.0
    orien_const.orientation.z = 0.0
    orien_const.orientation.w = 0.0

    orien_const.absolute_x_axis_tolerance = 0.2;
    orien_const.absolute_y_axis_tolerance = 0.2;
    orien_const.absolute_z_axis_tolerance = 3.14;
    orien_const.weight = 1.0;
    #--------------------------#

    #If down orientation is needed, constrain it
    if (request.orient):
        main(list_obj, end_goal, orien_const)
    else:
        main(list_obj, end_goal, None)


    return "Finished executing pose"  

def sawyer_server():
    # Initialize the server node for sawyer control
    rospy.init_node("sawyer_server")
    # Register service
    s = rospy.Service(
        "/sawyer_parms/enviro",  # Service name
        enviro,  # Service type
        sawyer_callback  # Service callback
    )
    rospy.loginfo('Running sawyer server...')
    rospy.spin() # Spin the node until Ctrl-C


if __name__ == '__main__':
    
    sawyer_server()

