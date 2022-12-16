#! /usr/bin/env python
# Copyright (c) 2013-2018, Rethink Robotics Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
SDK Joint Position Example: keyboard
"""
import argparse

import rospy

import intera_interface
import intera_external_devices

from intera_interface import CHECK_VERSION

import time

from robot_pos_sub import get_joint_states
from std_srvs.srv import Empty, SetBool
from planning.srv import forward_kinematics # Service type

# Seven joint angles to sent the robot to with FK
# global seven_angles
# seven_angles = {}

def map_keyboard(side):
    limb = intera_interface.Limb(side)

    try:
        gripper = intera_interface.Gripper(side + '_gripper')
    except:
        has_gripper = False
        rospy.loginfo("The electric gripper is not detected on the robot.")
    else:
        has_gripper = True

    joints = limb.joint_names()



    def set_j(limb, joint_name, delta):
        current_position = limb.joint_angle(joint_name)
        joint_command = {joint_name: current_position + delta}
        print("Executing" + str(joint_command))
        limb.set_joint_position_speed(0.3)
        limb.set_joint_positions(joint_command)

    def set_g(action):
        if has_gripper:
            if action == "close":
                gripper.close()
            elif action == "open":
                gripper.open()
            elif action == "calibrate":
                gripper.calibrate()

    def set_joint_angles(seven_angles):
        # print(seven_angles)
        # for key in seven_angles.keys():
        #     print(key + ": " + str(limb.joint_angle(key)))
        print("Moving")
        print("Moving ", seven_angles)
        for key in seven_angles.keys():
            while abs(limb.joint_angle(key) - float(seven_angles[key])) > 0.01:
                current_position = limb.joint_angle(key)
                command = {key: float(seven_angles[key])}
                print("Executing" + str(command))
                print("Current Angle: " +  str(limb.joint_angle(key)))
                print("Goal Angle: " + str(seven_angles[key]))
                limb.set_joint_position_speed(0.1)
                limb.set_joint_positions(command)
                time.sleep(0.1)


    # bindings = {
    #     '1': (set_j, [limb, joints[0], 0.1], joints[0]+" increase"),
    #     'q': (set_j, [limb, joints[0], -0.1], joints[0]+" decrease"),
    #     '2': (set_j, [limb, joints[1], 0.1], joints[1]+" increase"),
    #     'w': (set_j, [limb, joints[1], -0.1], joints[1]+" decrease"),
    #     '3': (set_j, [limb, joints[2], 0.1], joints[2]+" increase"),
    #     'e': (set_j, [limb, joints[2], -0.1], joints[2]+" decrease"),
    #     '4': (set_j, [limb, joints[3], 0.1], joints[3]+" increase"),
    #     'r': (set_j, [limb, joints[3], -0.1], joints[3]+" decrease"),
    #     '5': (set_j, [limb, joints[4], 0.1], joints[4]+" increase"),
    #     't': (set_j, [limb, joints[4], -0.1], joints[4]+" decrease"),
    #     '6': (set_j, [limb, joints[5], 0.1], joints[5]+" increase"),
    #     'y': (set_j, [limb, joints[5], -0.1], joints[5]+" decrease"),
    #     '7': (set_j, [limb, joints[6], 0.1], joints[6]+" increase"),
    #     'u': (set_j, [limb, joints[6], -0.1], joints[6]+" decrease")
    #  }
    # if has_gripper:
    #     bindings.update({
    #     '8': (set_g, "close", side+" gripper close"),
    #     'i': (set_g, "open", side+" gripper open"),
    #     '9': (set_g, "calibrate", side+" gripper calibrate")
    #     })
    done = False
    print("Controlling joints. Press ? for help, Esc to quit.")
    # while not done and not rospy.is_shutdown():
        # c = intera_external_devices.getch()
        # if c:
        #     # catch Esc or ctrl-c
        #     if c in ['\x1b', '\x03']:
        #         done = True
        #         rospy.signal_shutdown("Example finished.")
        #     else:
                # print("Running 7 joint angles:\n")
                # one = 0.51
                # two = 0
                # three = -1.15
                # four = 0.95
                # five = 0.80
                # six = -0.54
                # seven = 2
                # seven_angles = {
                #     joints[0]: one,
                #     joints[1]: two,
                #     joints[2]: three,
                #     joints[3]: four,
                #     joints[4]: five,
                #     joints[5]: six,
                #     joints[6]: seven,
                # }
        # print(seven_angles)
    print("Setting Angles")
    # print(seven_angles)
    set_joint_angles(seven_angles)

            # elif c in bindings:
            #     cmd = bindings[c]
            #     if c == '8' or c == 'i' or c == '9':
            #         cmd[0](cmd[1])
            #         print("command: %s" % (cmd[2],))
            #     else:
            #         #expand binding to something like "set_j(right, 'j0', 0.1)"
            #         cmd[0](*cmd[1])
            #         print("command: %s" % (cmd[2],))
            # else:
            #     print("key bindings: ")
            #     print("  Esc: Quit")
            #     print("  ?: Help")
            #     for key, val in sorted(list(bindings.items()),
            #                            key=lambda x: x[1][2]):
            #         print("  %s: %s" % (key, val[2]))



# def main():
#     """RSDK Joint Position Example: Keyboard Control

#     Use your dev machine's keyboard to control joint positions.

#     Each key corresponds to increasing or decreasing the angle
#     of a joint on Sawyer's arm. The increasing and descreasing
#     are represented by number key and letter key next to the number.
#     """
#     epilog = """
# See help inside the example with the '?' key for key bindings.
#     """
#     rp = intera_interface.RobotParams()
#     valid_limbs = rp.get_limb_names()
#     if not valid_limbs:
#         rp.log_message(("Cannot detect any limb parameters on this robot. "
#                         "Exiting."), "ERROR")
#         return
#     arg_fmt = argparse.RawDescriptionHelpFormatter
#     parser = argparse.ArgumentParser(formatter_class=arg_fmt,
#                                      description=main.__doc__,
#                                      epilog=epilog)
#     parser.add_argument(
#         "-l", "--limb", dest="limb", default=valid_limbs[0],
#         choices=valid_limbs,
#         help="Limb on which to run the joint position keyboard example"
#     )
#     args = parser.parse_args(rospy.myargv()[1:])

#     print("Initializing node... ")
#     rospy.init_node("sdk_joint_position_keyboard")
#     print("Getting robot state... ")
#     rs = intera_interface.RobotEnable(CHECK_VERSION)
#     init_state = rs.state().enabled

#     def clean_shutdown():
#         print("\nExiting example.")

#     rospy.on_shutdown(clean_shutdown)

#     rospy.loginfo("Enabling robot...")
#     rs.enable()
#     map_keyboard(args.limb)
#     print("Done.")

def set_joints_to_pour(request):
    # print("Initializing node... ")
    # rospy.init_node("fk_joint_position")
    global seven_angles
    print("Getting joint states")
    joint_states = get_joint_states().copy()
    print("3")
    if (not request.jitter):
        joint_states["right_j5"] = -0.5
        # joint_states["right_j1"] = -0.035
        print("In set pour", joint_states)

#     epilog = """
# See help inside the example with the '?' key for key bindings.
#     """
    # rp = intera_interface.RobotParams()
    # valid_limbs = rp.get_limb_names()
    # if not valid_limbs:
    #     rp.log_message(("Cannot detect any limb parameters on this robot. "
    #                     "Exiting."), "ERROR")
    #     return
    # arg_fmt = argparse.RawDescriptionHelpFormatter
    # parser = argparse.ArgumentParser(formatter_class=arg_fmt,
    #                                  description=main.__doc__,
    #                                  epilog=epilog)
    # parser.add_argument(
    #     "-l", "--limb", dest="limb", default=valid_limbs[0],
    #     choices=valid_limbs,
    #     help="Limb on which to run the joint position keyboard example"
    # )
    # args = parser.parse_args(rospy.myargv()[1:])

    
    # print("Getting robot state... ")
    # rs = intera_interface.RobotEnable(CHECK_VERSION)
    # init_state = rs.state().enabled

    # def clean_shutdown():
    #     print("\nExiting example.")

    # rospy.on_shutdown(clean_shutdown)

    # rospy.loginfo("Enabling robot...")
    # rs.enable()

        print("4")
        seven_angles = joint_states
        print("Seven Angles: ", seven_angles)
        fk = map_keyboard('right')
    else:
        joint_states["right_j5"] = -0.7 - request.offset * 0.1
        # joint_states["right_j1"] = -0.035
        print("In set pour", joint_states)
        print("4")
        seven_angles = joint_states
        print("Seven Angles: ", seven_angles)
        fk = map_keyboard('right')

        joint_states["right_j5"] = -0.5
        # joint_states["right_j1"] = -0.035
        print("In set pour", joint_states)
        print("4")
        seven_angles = joint_states
        print("Seven Angles: ", seven_angles)
        fk = map_keyboard('right')

        # fk.set_joint_angles(joint_states)

    # map_keyboard(args.limb)
    # print("Done.")

def forward_kinematics_callback(request):
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
    # rospy.loginfo("Got message request")
    # list_obj = []
    # end_goal = request.goal
    # print(request)
    # # print("goal", request.goal)
    # # print("name_obj", request.name_obj)

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
    set_joints_to_pour(request)
    print("Finished forward kinematics")

    return []

  

def forward_kinematics_server():
    # Initialize the server node for turtle1
    rospy.init_node("forward_kinematics_server")
    # Register service
    s = rospy.Service(
        "/forward_kinematics_positions",  # Service name
        forward_kinematics,  # Service type
        forward_kinematics_callback  # Service callback
    )
    rospy.loginfo('Running forward kinematics server...')
    rospy.spin() # Spin the node until Ctrl-C

if __name__ == '__main__':
    forward_kinematics_server()
    # set_joints_to_pour()
