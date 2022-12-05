#!/usr/bin/env python
from geometry_msgs.msg import Twist
import numpy as np
import rospy
from std_srvs.srv import Empty
import sys
from planning.srv import enviro  # Service type 1
from planning.srv import grip  # Service type 2
from planning.srv import scale  # Service type 3
# from turtlesim.srv import TeleportAbsolute
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped
from path_planner import PathPlanner