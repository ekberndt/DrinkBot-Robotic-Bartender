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


limb = intera_interface.Limb('right')
joints = limb.joint_names()

def set_joint_angles(seven_angles):
        print(seven_angles)
        for key in seven_angles.keys():
            print(key + ": " + str(limb.joint_angle(key)))
        for key in seven_angles.keys():
            while abs(limb.joint_angle(key) - float(seven_angles[key])) > 0.1:
                current_position = limb.joint_angle(key)
                command = {key: float(seven_angles[key])}
                print("Executing" + str(command))
                print("Current Angle: " +  str(limb.joint_angle(key)))
                print("Goal Angle: " + str(seven_angles[key]))
                limb.set_joint_position_speed(0.1)
                limb.set_joint_positions(command)
                time.sleep(0.1)
