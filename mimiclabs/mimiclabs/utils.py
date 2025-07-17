import os
import fcntl

import importlib

import mimiclabs
import mimiclabs.mimiclabs.macros as macros


def get_robosuite_version():
    """
    Returns the robosuite version as a string.
    """
    try:
        import robosuite

        return ".".join(robosuite.__version__.split(".")[:2])
    except ImportError:
        raise ImportError(
            "robosuite is not installed. Please install it to use this function."
        )


class disable_module_import:
    """
    Example usage:
        with disable_module_import("libero", "libero", "envs"):
            from libero.libero.envs.utils import *
    """

    def __init__(self, *modules):
        try:
            package_path = importlib.util.find_spec(
                modules[0]
            ).submodule_search_locations[0]
        except (ModuleNotFoundError, AttributeError):
            raise ImportError(
                f"Module {modules[0]} not found. Please ensure it is installed."
            )
        self.path = os.path.join(package_path, *modules[1:], "__init__.py")

        # Create a lock file to prevent multiple processes from modifying the same file.
        base_dir = os.path.join(macros.MIMICLABS_TMP_FOLDER, "locks")
        os.makedirs(base_dir, exist_ok=True)
        self._lock_file = os.path.join(base_dir, "_".join(modules) + ".lock")
        self._lock = None

    def __enter__(self):
        self._lock = open(self._lock_file, "w")
        fcntl.flock(self._lock, fcntl.LOCK_EX)
        if os.path.exists(self.path):
            os.rename(self.path, self.path + ".bak")

    def __exit__(self, exc_type, exc_value, traceback):
        if os.path.exists(self.path + ".bak"):
            os.rename(self.path + ".bak", self.path)
        fcntl.flock(self._lock, fcntl.LOCK_UN)
        self._lock.close()
