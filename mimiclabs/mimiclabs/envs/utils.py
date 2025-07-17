import numpy as np
from transforms3d import euler

from ..utils import disable_module_import

with disable_module_import("libero", "libero", "envs"):
    from libero.libero.envs.utils import *


def convert_spherical_to_pos_quat(r_theta_phi):
    """
    Converts spherical coordinates (physics convention) into Euclidean position
    and quaternion rotation, such that -z points at the origin.
    """
    r, theta, phi = r_theta_phi
    pos = [
        r * np.sin(theta) * np.cos(phi),
        r * np.sin(theta) * np.sin(phi),
        r * np.cos(theta),
    ]
    euler_zxy = (np.pi / 2 + phi, theta, 0)
    quat_wxyz = euler.euler2quat(*euler_zxy, axes="rzxy")
    return pos, quat_wxyz
