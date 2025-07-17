from ...utils import disable_module_import

from .base_region_sampler import *

with disable_module_import("libero", "libero", "envs"):
    from libero.libero.envs.regions.workspace_region_sampler import *
    from libero.libero.envs.regions.object_property_sampler import *


REGION_SAMPLERS = {
    "mimiclabs_lab1_tabletop_manipulation": {"table": Libero100TableRegionSampler},
    "mimiclabs_lab2_tabletop_manipulation": {"table": Libero100TableRegionSampler},
    "mimiclabs_lab3_tabletop_manipulation": {"table": Libero100TableRegionSampler},
    "mimiclabs_lab4_tabletop_manipulation": {"table": Libero100TableRegionSampler},
    "mimiclabs_lab5_tabletop_manipulation": {"table": Libero100TableRegionSampler},
    "mimiclabs_lab6_tabletop_manipulation": {"table": Libero100TableRegionSampler},
    "mimiclabs_lab7_tabletop_manipulation": {"table": Libero100TableRegionSampler},
    "mimiclabs_lab8_tabletop_manipulation": {"table": Libero100TableRegionSampler},
}


def get_region_samplers(problem_name, region_sampler_name):
    return REGION_SAMPLERS[problem_name][region_sampler_name]
