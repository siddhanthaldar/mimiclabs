# Data Collection

We support data collection using a Meta Quest and a SpaceMouse in MimicLabs. Please follow instructions in `docs/getting_started/setup_devices.md` to setup your device before collecting expert demonstrations for the tasks your created.

## Collecting expert demonstrations

After having set up your task config, use our provided script to collect demonstrations for your task:
```bash
$ cd <PATH_TO_THIS_REPO>/mimiclabs/data_collection/sim
$ python scripts/collect_data.py \
    --task_suite_name <YOUR/TASK/SUITE> \
    --task_name <TASK_NAME> \
    --robots Panda \
    --control_delta \
    --device <DEVICE_NAME>
```

<div class="admonition note">
    <p class="admonition-title">Note: front-view render during demo collection</p>
    While the rendered view during demo collection is front-view for ease of demo collection, demos being stored will render using agent-view camera specified in the task BDDL. 
</div>

For example, you can replace `<YOUR/TASK/SUITE>` with `example_suite` and `<TASK_NAME>` with `example_task`. This will spin-up data collection for the task config located at `mimiclabs/task_suites/test_siute/example_task.bddl` in this repo. Note that `<YOUR/TASK/SUITE>` can be a directory tree and does not necessarily have to be a single directory.

You can specify your choice of device by replacing `<DEVICE_NAME>` with `spacemouse` or `quest`.

By default, demos will be stored under `<PATH_TO_THIS_REPO>/mimiclabs/data_collection/sim/demos/<YOUR/TASK/SUITE>/<TASK_NAME>`.

Once collected, run the following script to post-process demos and save them into a single hdf5 file.
```bash
$ python scripts/postprocess_demos.py --demo_dir <PATH/TO/COLLECTED/DEMOS>
```

To expand the collected source demonstrations, follow instructions in the next tutorial.

## Controls

### Meta Quest

- Right controller: move robot
- Left controller: move second robot (if applicable)
- A button: save demo at any stage (saving also automatically happens when task is done)
- B button: delete current demo, and start a new one
- ctrl+C: discard current demo and exit

### SpaceMouse

- Joystick: move robot
- Right button: start data collection / discard demo
- Left button: toggle gripper
- ctrl+C: discard current demo and exit

<div class="admonition warning">
<p class="admonition-title">Warning: issues with hid on MacOS</p>

Some users may face issues locating hid binaries on MacOS. Providing the `DYLD_LIBRARY_PATH` before the python command, such as `DYLD_LIBRARY_PATH=/opt/homebrew/lib python ...`, may help resolve the issue.

</div>

## Playing back collected demonstrations

You might want to play back your collected demonstrations to make sure they are stored properly and can be reproduced given all saved simulation parameters. We provide a script to do this.

```bash
python scripts/playback_demo.py \
    --dataset_path <PATH/TO/DEMO/FILE> \
    --control_delta \
    --video_dir <PATH/TO/VIDEO/DIR> \
    --render
```

For example, you can replace `<PATH/TO/DEMO/FILE>` with `./demos/example_suite/example_task/demo_0.hdf5` which can the first demonstration collected for a test task, `<PATH/TO/VIDEO/DIR>` with `./demos/example_suite/example_task/playback` as a temporary directory to store playback videos. The `--control_delta` flag directs the script to play back delta actions. Skipping this flag will replay absolute actions. The `--render` flag forces rendering to screen.

<div class="admonition warning">
<p class="admonition-title">Warning: trying to playback absolute actions</p>

Absolute actions stored in collected demonstrations are absolute poses extracted from delta commands. Based on the device and control parameters used for data collection, absolute commands may or may not be able to produce expected results. 

For example, for the default control parameters for a SpaceMouse agent that clip delta commands, and data collected using a delta controller, played back absolute commands might overshoot while delta commands would replicate exact same behavior as was demonstrated. For the Meta Quest agent however, our default parameters have no action clipping, and hence absolute commands will replicate demonstrated behavior even if data collection was done using a delta controller.

</div>
