#!/usr/bin/env python
from geometry_msgs.msg import Twist
import numpy as np
import rospy
from std_srvs.srv import Empty # Service type
import sys
from planning.srv import enviro # Service type
from path_test import main #Link to Arm Movement
from moveit_msgs.msg import OrientationConstraint, PositionConstraint
from geometry_msgs.msg import PoseStamped
from path_planner import PathPlanner

name = ""
def sawyer_callback(request):
    ## rospy.wait_for_service('clear')
    # rospy.wait_for_service("/{}/teleport_absolute".format(name))
    ## clear_proxy = rospy.ServiceProxy('clear', Empty)
    # teleport_proxy = rospy.ServiceProxy(
    #     "/{}/teleport_absolute".format(name),
    #     TeleportAbsolute
    # )
    # pub = rospy.Publisher(
    #     "/{}/cmd_vel".format(name), Twist, queue_size=50)

    # Publish to cmd_vel at 5 Hz
    # rate = rospy.Rate(5)

    # Clear historical path traces
    rospy.loginfo("Got message request")
    list_obj = []
    end_goal = request.goal
    print(request)
    # print("goal", request.goal)
    # print("name_obj", request.name_obj)

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
    #Create a path constraint for the arm
    #UNCOMMENT FOR THE ORIENTATION CONSTRAINTS PART
    #TODO: add conditional taken from srv msg
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

    # pos_const = PositionConstraint()
    # pos_const.link_name = "right_gripper_tip";
    # pos_const.header.frame_id = "base";
    # pos_const.target_point_offset.x = 0.6;
    # pos_const.target_point_offset.y = -0.3;
    # pos_const.target_point_offset.z = 0.0;
    # pos_const.weight = 1.0;

    #POSITION CONSTRAINT TO PICK UP CUP
    # pos_const = PositionConstraint()


    #If down orientation is needed, constrain it
    
    if (request.orient):
        main(list_obj, end_goal, orien_const)
        
    else:
        main(list_obj, end_goal, None)


    return "Finished executing pose"  # This line will never be reached

def sawyer_server():
    # Initialize the server node for turtle1
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
    # name = "turtle1"
    # if len(sys.argv) == 2:
    #     name = sys.argv[1]
    sawyer_server()

