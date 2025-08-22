"""
Script to generate MimicGen config classes and json templates, one per task bddl in the provided task suite.

Example usage:

python scripts/generate_configs_and_jobs.py \
    --task_suite_name example_suite \
    --source_demos_dir ../data_collection/sim/demos/example_suite/ \
    --generation_dir ./data/example_suite/ \
    --num_demos 50
"""

import os
import argparse
from termcolor import colored
from pathlib import Path

from mimicgen.configs.config import get_all_registered_configs

import mimiclabs
from mimiclabs.mimicgen.config import generate_mg_config_classes


def generate_config_templates(args):
    """
    Generates config templates for MimicGen data generation for all BDDL files
    under args.task_suite_name.
    """
    # directory for storing template config jsons
    target_dir = os.path.join(
        mimiclabs.__path__[0], "mimicgen", "exps", args.task_suite_name
    )

    # check if target_dir exists and prompt before overriding
    if os.path.exists(target_dir):
        inp = input(
            f"Directory {target_dir} already exists. Would you like to overwrite it? y/n\n"
        )
        if inp.lower() not in ["y", "yes"]:
            print("Exiting without generating config templates.")
            return target_dir

    # get all registered config classes
    all_configs = get_all_registered_configs()
    # store config json by config type
    os.makedirs(target_dir, exist_ok=True)
    for name in all_configs[args.task_suite_name]:
        # make config class to dump it to json
        c = all_configs[args.task_suite_name][name]()
        assert name == c.NAME
        assert args.task_suite_name == c.TYPE

        # change config params based on args
        c.experiment.source.dataset_path = os.path.join(
            args.source_demos_dir, name, "demo.hdf5"
        )
        if not os.path.exists(c.experiment.source.dataset_path):
            print(f"Source demos not found at {c.experiment.source.dataset_path}")
            continue
        # assert os.path.exists(
        #     c.experiment.source.dataset_path
        # ), f"Source demos not found at {c.experiment.source.dataset_path}"
        c.experiment.generation.path = os.path.join(args.generation_dir, name)
        c.experiment.generation.guarantee = True
        c.experiment.generation.num_trials = args.num_demos
        c.experiment.max_num_failures = args.max_num_failures
        c.experiment.num_demo_to_render = args.num_demo_to_render
        c.experiment.num_fail_demo_to_render = args.num_fail_demo_to_render
        c.experiment.source.n = args.limit_source_demos
        c.experiment.generation.select_src_per_subtask = args.select_src_per_subtask

        # dump to json
        json_path = os.path.join(target_dir, f"{name}.json")
        c.dump(filename=json_path)
    return target_dir


def main(args):
    generate_mg_config_classes(
        args.task_suite_name, args.camera_names, args.camera_height, args.camera_width
    )
    config_dir = generate_config_templates(args)
    print(colored(f"Generated config templates", "green"), f"--> {config_dir}")

    with open(os.path.join(config_dir, "jobs.sh"), "w") as f:
        f.write("#!/bin/bash\n")
        for config_file in os.listdir(config_dir):
            if config_file.endswith(".json"):
                f.write(
                    f"python scripts/generate_dataset.py --config {os.path.join(config_dir, config_file)} --auto-remove-exp &\n"
                )

    print(
        colored(f"Exported datagen jobs", "green"),
        f"--> {os.path.join(config_dir, 'jobs.sh')}",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--task_suite_name",
        type=str,
        required=True,
        help="name of task suite to generate demos for",
    )
    parser.add_argument(
        "--source_demos_dir",
        type=str,
        required=True,
        help="directory containing source demos for the task suite, one subdirectory per task bddl file",
    )
    parser.add_argument(
        "--generation_dir",
        type=str,
        required=True,
        help="directory to store generated demos for the task suite, one subdirectory per task bddl file",
    )
    parser.add_argument(
        "--num_demos",
        type=int,
        required=True,
        help="number of demos to generate for each task bddl",
    )
    parser.add_argument(
        "--max_num_failures",
        type=int,
        default=25,
    )
    parser.add_argument(
        "--num_demo_to_render",
        type=int,
        default=10,
    )
    parser.add_argument(
        "--num_fail_demo_to_render",
        type=int,
        default=25,
    )
    parser.add_argument(
        "--limit_source_demos",
        type=int,
        default=None,
        help="if provided, limits data generation to using only that many source demos",
    )
    parser.add_argument(
        "--select_src_per_subtask",
        type=bool,
        default=True,
        help="if True, select a different source demonstration for each subtask during data generation, else keep the same one for the entire episode",
    )
    # below args are used for config class generation
    parser.add_argument(
        "--camera_names",
        type=str,
        required=False,
        nargs="+",
        default=["agentview", "robot0_eye_in_hand"],
        help="camera names to use for rendering",
    )
    parser.add_argument(
        "--camera_height",
        type=int,
        help="camera height to use for rendering",
        default=84,
    )
    parser.add_argument(
        "--camera_width",
        type=int,
        help="camera width to use for rendering",
        default=84,
    )

    args = parser.parse_args()
    main(args)
