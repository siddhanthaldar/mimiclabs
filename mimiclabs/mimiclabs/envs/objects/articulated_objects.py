import os
import re
import numpy as np

from dataclasses import dataclass
from robosuite.models.objects import MujocoXMLObject

from libero.libero.envs.base_object import (
    register_visual_change_object,
    register_object,
)

from mimiclabs.mimiclabs import assets_root


class ArticulatedObject(MujocoXMLObject):
    def __init__(self, name, obj_name, joints=[dict(type="free", damping="0.0005")]):
        super().__init__(
            os.path.join(str(assets_root), f"articulated_objects/{obj_name}.xml"),
            name=name,
            joints=joints,
            obj_type="all",
            duplicate_collision_geoms=False,
        )
        self.category_name = "_".join(
            re.sub(r"([A-Z])", r" \1", self.__class__.__name__).split()
        ).lower()
        self.rotation = (np.pi / 4, np.pi / 2)
        self.rotation_axis = "x"

        articulation_object_properties = {
            "default_open_ranges": [],
            "default_close_ranges": [],
        }
        self.object_properties = {
            "articulation": articulation_object_properties,
            "vis_site_names": {},
        }

    def is_open(self, qpos):
        raise NotImplementedError

    def is_close(self, qpos):
        raise NotImplementedError


@register_object
class Microwave2(ArticulatedObject):
    def __init__(
        self,
        name="microwave_2",
        obj_name="microwave_2",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)

        self.object_properties["articulation"]["default_open_ranges"] = [-2.094, -1.3]
        self.object_properties["articulation"]["default_close_ranges"] = [-0.005, 0.0]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class Microwave3(ArticulatedObject):
    def __init__(
        self,
        name="microwave_3",
        obj_name="microwave_3",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)

        self.object_properties["articulation"]["default_open_ranges"] = [-2.094, -1.3]
        self.object_properties["articulation"]["default_close_ranges"] = [-0.005, 0.0]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class Microwave4(ArticulatedObject):
    def __init__(
        self,
        name="microwave_4",
        obj_name="microwave_4",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)

        self.object_properties["articulation"]["default_open_ranges"] = [-2.094, -1.3]
        self.object_properties["articulation"]["default_close_ranges"] = [-0.005, 0.0]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class Microwave5(ArticulatedObject):
    def __init__(
        self,
        name="microwave_5",
        obj_name="microwave_5",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)

        self.object_properties["articulation"]["default_open_ranges"] = [-2.094, -1.3]
        self.object_properties["articulation"]["default_close_ranges"] = [-0.005, 0.0]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class Microwave6(ArticulatedObject):
    def __init__(
        self,
        name="microwave_6",
        obj_name="microwave_6",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)

        self.object_properties["articulation"]["default_open_ranges"] = [-2.094, -1.3]
        self.object_properties["articulation"]["default_close_ranges"] = [-0.005, 0.0]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class Microwave7(ArticulatedObject):
    def __init__(
        self,
        name="microwave_7",
        obj_name="microwave_7",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)

        self.object_properties["articulation"]["default_open_ranges"] = [-2.094, -1.3]
        self.object_properties["articulation"]["default_close_ranges"] = [-0.005, 0.0]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class Microwave8(ArticulatedObject):
    def __init__(
        self,
        name="microwave_8",
        obj_name="microwave_8",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)

        self.object_properties["articulation"]["default_open_ranges"] = [-2.094, -1.3]
        self.object_properties["articulation"]["default_close_ranges"] = [-0.005, 0.0]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class MarbleCabinet(ArticulatedObject):
    def __init__(
        self,
        name="marble_cabinet",
        obj_name="marble_cabinet",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.object_properties["articulation"]["default_open_ranges"] = [-0.16, -0.14]
        self.object_properties["articulation"]["default_close_ranges"] = [0.0, 0.005]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class ColorfulCabinet(ArticulatedObject):
    def __init__(
        self,
        name="colorful_cabinet",
        obj_name="colorful_cabinet",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.object_properties["articulation"]["default_open_ranges"] = [-0.16, -0.14]
        self.object_properties["articulation"]["default_close_ranges"] = [0.0, 0.005]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class LavaCabinet(ArticulatedObject):
    def __init__(
        self,
        name="lava_cabinet",
        obj_name="lava_cabinet",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.object_properties["articulation"]["default_open_ranges"] = [-0.16, -0.14]
        self.object_properties["articulation"]["default_close_ranges"] = [0.0, 0.005]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class LightWoodCabinet(ArticulatedObject):
    def __init__(
        self,
        name="light_wood_cabinet",
        obj_name="light_wood_cabinet",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.object_properties["articulation"]["default_open_ranges"] = [-0.16, -0.14]
        self.object_properties["articulation"]["default_close_ranges"] = [0.0, 0.005]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class BlueCabinet(ArticulatedObject):
    def __init__(
        self,
        name="blue_cabinet",
        obj_name="blue_cabinet",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.object_properties["articulation"]["default_open_ranges"] = [-0.16, -0.14]
        self.object_properties["articulation"]["default_close_ranges"] = [0.0, 0.005]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False


@register_object
class MetalCabinet(ArticulatedObject):
    def __init__(
        self,
        name="metal_cabinet",
        obj_name="metal_cabinet",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.object_properties["articulation"]["default_open_ranges"] = [-0.16, -0.14]
        self.object_properties["articulation"]["default_close_ranges"] = [0.0, 0.005]

    def is_open(self, qpos):
        if qpos < max(self.object_properties["articulation"]["default_open_ranges"]):
            return True
        else:
            return False

    def is_close(self, qpos):
        if qpos > min(self.object_properties["articulation"]["default_close_ranges"]):
            return True
        else:
            return False
