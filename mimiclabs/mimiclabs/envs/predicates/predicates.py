from ...utils import disable_module_import

with disable_module_import("libero", "libero", "envs"):
    from libero.libero.envs.predicates.base_predicates import *


class Grasp(UnaryAtomic):
    def __call__(self, arg1):
        return arg1.check_grasp()

class NoGrasp(UnaryAtomic):
    def __call__(self, arg1):
        return not arg1.check_grasp_tolerant()
