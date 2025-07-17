import json
import argparse

from mimicgen.scripts.generate_dataset import main as MG_generate_dataset

from mimiclabs.mimicgen.config import generate_mg_config_classes


def main(args):
    config = json.load(open(args.config))
    task_suite_name = config["type"]
    generate_mg_config_classes(
        task_suite_name,
        config["obs"]["camera_names"],
        config["obs"]["camera_height"],
        config["obs"]["camera_width"],
    )
    MG_generate_dataset(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="path to MimicGen config json",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="set this flag to run a quick generation run for debugging purposes",
    )
    parser.add_argument(
        "--auto-remove-exp",
        action="store_true",
        help="force delete the experiment folder if it exists",
    )
    parser.add_argument(
        "--render",
        action="store_true",
        help="render each data generation attempt on-screen",
    )
    parser.add_argument(
        "--video_path",
        type=str,
        default=None,
        help="if provided, render the data generation attempts to the provided video path",
    )
    parser.add_argument(
        "--video_skip",
        type=int,
        default=5,
        help="skip every nth frame when writing video",
    )
    parser.add_argument(
        "--render_image_names",
        type=str,
        nargs="+",
        default=None,
        help="(optional) camera name(s) / image observation(s) to use for rendering on-screen or to video. Default is"
        "None, which corresponds to a predefined camera for each env type",
    )
    parser.add_argument(
        "--pause_subtask",
        action="store_true",
        help="pause after every subtask during generation for debugging - only useful with render flag",
    )
    parser.add_argument(
        "--source",
        type=str,
        help="path to source dataset, to override the one in the config",
    )
    parser.add_argument(
        "--task_name",
        type=str,
        help="environment name to use for data generation, to override the one in the config",
        default=None,
    )
    parser.add_argument(
        "--folder",
        type=str,
        help="folder that will be created with new data, to override the one in the config",
        default=None,
    )
    parser.add_argument(
        "--num_demos",
        type=int,
        help="number of demos to generate, or attempt to generate, to override the one in the config",
        default=None,
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="seed, to override the one in the config",
        default=None,
    )

    args = parser.parse_args()
    main(args)
