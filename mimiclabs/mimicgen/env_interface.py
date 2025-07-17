import numpy as np

from mimicgen.env_interfaces.robosuite import RobosuiteInterface
import mimicgen.utils.pose_utils as PoseUtils


class MG_MimicLabs(RobosuiteInterface):
    """
    A general MimicGen environment interface for MimicLabs tasks.
    """

    @staticmethod
    def _get_term_signal_key_from_demo_state(demo_state, prefix=None, suffix=None):
        key = "_".join(demo_state)
        if prefix:
            key = f"{prefix}_{key}"
        if suffix:
            key = f"{key}_{suffix}"
        return key

    def get_object_poses(self):
        """
        Returns poses of objects and fixtures in the environment.
        Currently does not include site objects.
        """
        object_poses = dict()
        for obj_name in self.env.objects_dict:
            obj_id = self.env.obj_body_id[obj_name]
            obj_pos = np.array(self.env.sim.data.body_xpos[obj_id])
            obj_rot = np.array(self.env.sim.data.body_xmat[obj_id].reshape(3, 3))
            object_poses[obj_name] = PoseUtils.make_pose(obj_pos, obj_rot)
        for obj_name in self.env.fixtures_dict:
            obj_id = self.env.obj_body_id[obj_name]
            obj_pos = np.array(self.env.sim.data.body_xpos[obj_id])
            obj_rot = np.array(self.env.sim.data.body_xmat[obj_id].reshape(3, 3))
            object_poses[obj_name] = PoseUtils.make_pose(obj_pos, obj_rot)
        return object_poses

    def get_subtask_term_signals(self):
        # Using partial metrics checks for all provided predicates
        signals = dict()
        subtask_predicates = self.env.parsed_problem["demonstration_states"]
        for i, subtask_predicate in enumerate(subtask_predicates):
            subtask_id = f"subtask_{i+1}"
            subtask_key = self._get_term_signal_key_from_demo_state(
                subtask_predicate, prefix=subtask_id
            )
            signals[subtask_key] = int(self.env._eval_predicate(subtask_predicate))
        return signals
