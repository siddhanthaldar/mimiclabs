from ...utils import disable_module_import

with disable_module_import("libero", "libero", "envs"):
    from libero.libero.envs.regions.base_region_sampler import *


class MultiRegionRandomSamplerWithYaw(MultiRegionRandomSampler):
    def __init__(
        self,
        name,
        mujoco_objects=None,
        x_ranges=[(0, 0)],
        y_ranges=[(0, 0)],
        rotation=None,
        rotation_axis="z",
        ensure_object_boundary_in_range=True,
        ensure_valid_placement=True,
        reference_pos=(0, 0, 0),
        z_offset=0.0,
    ):
        super().__init__(
            name,
            mujoco_objects,
            x_ranges,
            y_ranges,
            rotation,
            rotation_axis,
            ensure_object_boundary_in_range,
            ensure_valid_placement,
            reference_pos,
            z_offset,
        )
        self.rotations = copy(self.rotation)
        self.rotation = self.rotations[self.idx]

    def _sample_quat(self):
        self.rotation = self.rotations[self.idx]
        return super()._sample_quat()
