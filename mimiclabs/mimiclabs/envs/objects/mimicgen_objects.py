import os
import re
import numpy as np

from dataclasses import dataclass
from robosuite.models.objects import MujocoXMLObject
import xml.etree.ElementTree as ET
from easydict import EasyDict

from libero.libero.envs.base_object import (
    register_object,
)

from mimicgen.models.robosuite.objects import (
    CoffeeMachineObject,
    CoffeeMachinePodObject,
)


@register_object
class CoffeePod(CoffeeMachinePodObject):
    def __init__(
        self,
        name="coffee_pod",
        obj_name="coffee_pod",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name=name)

        self.category_name = "mimicgen_object"
        self.rotation = (0, 0)
        self.rotation_axis = "x"
        self.object_properties = {"vis_site_names": {}}


@register_object
class CoffeeMachine(CoffeeMachineObject):
    def __init__(
        self,
        name="coffee_machine",
        obj_name="coffee_machine",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name=name)
        _obj = self.get_obj()

        # Add pod_region site to object
        coffee_pod_holder = _obj.find(f".//body[@name='{self.name}_pod_holder_root']")
        pod_holder_size = " ".join(
            [s.strip() for s in str(tuple(self.pod_holder_size))[1:-1].split(",")]
        )
        site_str = f"<site \
            name='{self.name}_pod_region' \
            type='box' \
            pos='{coffee_pod_holder.get('pos')}' \
            quat='{coffee_pod_holder.get('quat')}' \
            size='{pod_holder_size}' \
            rgba='0.8 0.8 0.8 0' \
            group='0' \
            />"
        site_obj = ET.fromstring(site_str)
        # append site to root object
        _obj.append(site_obj)

        self.category_name = "mimicgen_object"
        self.rotation = None  # (0, 0) # get from bddl
        self.rotation_axis = "x"

        hinge_tol = 15.0 * np.pi / 180.0
        articulation_object_properties = {
            "default_open_ranges": [(2 * np.pi / 3) - hinge_tol, 2 * np.pi / 3],
            "default_close_ranges": [0, hinge_tol],
        }
        self.object_properties = {
            "articulation": articulation_object_properties,
            "vis_site_names": {},
        }
        self.object_state_joints = [super().joints[1]]

    @property
    def joints(self):
        return [super().joints[0]]  # return free joint

    def is_open(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False
