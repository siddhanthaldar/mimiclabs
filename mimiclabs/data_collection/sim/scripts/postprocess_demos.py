"""
This script is used to postprocess demos collected using the data collection scripts.
It merges all hdf5 files in a directory into a single hdf5 file.

Example usage:
    python scripts/postprocess_demos.py \
        --demo_dir ./demos/example_suite/example_task/
        
"""

import argparse

from mimiclabs.data_collection.sim.demo_saver import DemoSaver


def main(args):
    DemoSaver.merge_hdf5s(args.demo_dir, verbose=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo_dir", type=str, required=True)
    args = parser.parse_args()
    main(args)
