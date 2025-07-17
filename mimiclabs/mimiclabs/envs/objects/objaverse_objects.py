import os
import numpy as np
import re

from robosuite.models.objects import MujocoXMLObject
from robosuite.utils.mjcf_utils import xml_path_completion

import pathlib

absolute_path = pathlib.Path(__file__).parent.parent.parent.absolute()

from libero.libero.envs.base_object import (
    register_visual_change_object,
    register_object,
)


class ObjaverseObject(MujocoXMLObject):
    def __init__(self, name, obj_name, joints=[dict(type="free", damping="0.0005")]):
        super().__init__(
            os.path.join(
                str(absolute_path),
                f"assets/objects/objaverse_objects/{obj_name}/{obj_name}.xml",
            ),
            name=name,
            joints=joints,
            obj_type="all",
            duplicate_collision_geoms=True,
        )
        self.category_name = "_".join(
            re.sub(r"([A-Z])", r" \1", self.__class__.__name__).split()
        ).lower()
        self.rotation = (np.pi / 2, np.pi / 2)
        self.rotation_axis = "x"
        self.object_properties = {"vis_site_names": {}}


@register_object
class ObjaverseBanana(ObjaverseObject):
    def __init__(self, name="objaverse_banana", obj_name="banana"):
        super().__init__(name, obj_name)


@register_object
class ObjaverseApple(ObjaverseObject):
    def __init__(self, name="objaverse_apple", obj_name="apple"):
        super().__init__(name, obj_name)


@register_object
class ObjaverseMug(ObjaverseObject):
    def __init__(self, name="objaverse_mug", obj_name="mug"):
        super().__init__(name, obj_name)


@register_object
class ObjaverseNotebook(ObjaverseObject):
    def __init__(self, name="objaverse_notebook", obj_name="notebook"):
        super().__init__(name, obj_name)


@register_object
class ObjaverseCap(ObjaverseObject):
    def __init__(self, name="objaverse_cap", obj_name="cap"):
        super().__init__(name, obj_name)


@register_object
class ObjaverseCan(ObjaverseObject):
    def __init__(self, name="objaverse_can", obj_name="can"):
        super().__init__(name, obj_name)
