"""
Script to add MimicGen-specific info to a source dataset.

Example usage:
    python scripts/prepare_src_dataset.py \
        --dataset /path/to/src_dataset.hdf5
"""

import os
import json
import h5py
import argparse
from termcolor import colored

from mimicgen.scripts.prepare_src_dataset import prepare_src_dataset

import mimiclabs.mimiclabs.envs.bddl_utils as BDDLUtils
from mimiclabs.mimicgen.env_interface import *


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="path to input hdf5 dataset, which will be modified in-place",
    )
    parser.add_argument(
        "--env_interface",
        type=str,
        default="MG_MimicLabs",  # default to mimiclabs
        help="name of environment interface class to use for this source dataset",
    )
    parser.add_argument(
        "--env_interface_type",
        type=str,
        default="robosuite",  # default to robosuite
        help="type of environment interface to use for this source dataset",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=None,
        help="(optional) stop after n trajectories are processed",
    )
    parser.add_argument(
        "--filter_key",
        type=str,
        default=None,
        help="(optional) name of filter key, to select a subset of demo keys in the source hdf5",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="(optional) path to output hdf5 dataset, instead of modifying existing dataset in-place",
    )

    args = parser.parse_args()

    assert args.dataset.endswith(".hdf5"), "Input dataset must be an hdf5 file."

    # issue warnings pertaining to information that may be missing in the task config
    with h5py.File(args.dataset, "r") as f:
        env_meta = json.loads(f["data"].attrs["env_args"])
        bddl_file_name = env_meta["env_kwargs"]["bddl_file_name"]

        # get path of bddl in current repo
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        parent_dir = os.path.dirname(parent_dir)
        bddl_name = bddl_file_name.split("/")[-1]
        bddl_file_name = os.path.join(parent_dir, "mimiclabs", "task_suites", "individual_objects_suite", bddl_name)

        parsed_problem = BDDLUtils.robosuite_parse_problem(bddl_file_name)
        if len(parsed_problem["demonstration_states"]) == 0:
            print(
                colored(
                    "[mimiclabs WARNING] No subtask predicates found in the BDDL parsed problem. Did you specify demonstration predicates in your task config?",
                    "yellow",
                )
            )

    prepare_src_dataset(
        dataset_path=args.dataset,
        env_interface_name=args.env_interface,
        env_interface_type=args.env_interface_type,
        filter_key=args.filter_key,
        n=args.n,
        output_path=args.output,
    )
