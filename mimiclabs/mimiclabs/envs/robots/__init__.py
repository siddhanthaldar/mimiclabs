from ...utils import get_robosuite_version

from .mounted_panda import MountedPanda

import robosuite

if get_robosuite_version() == "1.4":
    from robosuite.robots.single_arm import SingleArm as RobosuiteRobot
else:
    from robosuite.robots import FixedBaseRobot as RobosuiteRobot
from robosuite.robots import ROBOT_CLASS_MAPPING

ROBOT_CLASS_MAPPING.update({"MountedPanda": RobosuiteRobot})
