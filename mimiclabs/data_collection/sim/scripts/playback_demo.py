"""
Script to playback a demo from a dataset. Stores video of the playback if save_video is True.

Example usage:
python scripts/playback_demo.py \
    --dataset_path ./demos/example_suite/example_task/demo_0.hdf5 \
    --control_delta \
    --video_dir ./demos/example_suite/example_task/playback/ \
    --render
"""

import json
import h5py
import argparse
import imageio
import numpy as np
import matplotlib.pyplot as plt

import robosuite

from mimiclabs.mimiclabs.envs.problems import *


def main(args):
    dataset = h5py.File(args.dataset_path, "r")

    env_args = json.loads(dataset["data"].attrs["env_args"])
    env_name = env_args["env_name"]
    env_kwargs = env_args["env_kwargs"]

    # force screen rendering
    env_kwargs["has_renderer"] = args.render

    # override controller config from args
    if args.control_delta is not None:
        # NOTE(VS) this currently does not support robosuite v1.5
        if not isinstance(env_kwargs["controller_configs"], list):
            env_kwargs["controller_configs"] = [env_kwargs["controller_configs"]]
        for i in range(len(env_kwargs["controller_configs"])):
            env_kwargs["controller_configs"][i]["control_delta"] = args.control_delta

    env = robosuite.make(env_name, **env_kwargs)
    env.reset()

    demos = sorted(list(dataset["data"].keys()), key=lambda x: int(x.split("_")[-1]))
    print(f"Found {len(demos)} demos in dataset")
    if args.num_demos is not None:
        demos = demos[: args.num_demos]
        print(f"Playing back {args.num_demos} demo(s)")

    for demo_id in demos:
        print(f"Playing back demo {demo_id}")

        # reset env to the state in the dataset
        states = dataset[f"data/{demo_id}/states"][0]
        model_file = dataset[f"data/{demo_id}"].attrs["model_file"]
        env.reset_to({"states": states, "model": model_file})
        if args.render:
            env.render()

        if env_kwargs["controller_configs"][0]["control_delta"]:
            actions = dataset[f"data/{demo_id}/actions"]
        else:
            actions = dataset[f"data/{demo_id}/actions_abs"]

        demo_len = len(actions)

        # save video
        video_writer = None
        if args.video_dir is not None:
            os.makedirs(args.video_dir, exist_ok=True)
            video_path = f"{args.video_dir}/{demo_id}.mp4"
            video_writer = imageio.get_writer(video_path, fps=20)

        for t in range(demo_len):
            env.step(actions[t])
            if args.render:
                env.render()  # render to screen

            if (video_writer is not None) and (t % args.video_skip == 0):
                imgs = []

                # writing agentview image
                imgs.append(
                    env.sim.render(height=320, width=320, camera_name="agentview")[::-1]
                )

                # writing to video
                video_writer.append_data(
                    np.concatenate(imgs, axis=0)
                )  # concat along height


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, required=True)
    parser.add_argument(
        "--control_delta",
        action="store_true",
        help="whether to control robot using delta actions during playback",
    )
    parser.add_argument(
        "--num_demos",
        type=int,
        default=1,
        help="limit the number of demos to play back",
    )
    parser.add_argument("--video_dir", type=str, default=None)
    parser.add_argument("--video_skip", type=int, default=1)
    parser.add_argument(
        "--render",
        action="store_true",
        help="whether to render the environment to screen",
    )
    args = parser.parse_args()
    main(args)
