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

    done = False
    print("Controlling joints. Press ? for help, Esc to quit.")
    print("Setting Angles")
    set_joint_angles(seven_angles)

def set_joints_to_pour(request):
    global seven_angles
    print("Getting joint states")
    joint_states = get_joint_states().copy()
    if (not request.jitter):
        joint_states["right_j5"] = -0.5
        print("In set pour", joint_states)
        seven_angles = joint_states
        fk = map_keyboard('right')
    else:
        joint_states["right_j5"] = -0.7 - request.offset * 0.1
        print("In set pour", joint_states)
        seven_angles = joint_states
        fk = map_keyboard('right')

        joint_states["right_j5"] = -0.5
        print("In set pour", joint_states)
        seven_angles = joint_states
        fk = map_keyboard('right')

def forward_kinematics_callback(request):
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
