################################ DATA COLLECTION ################################

cd mimiclabs/data_collection/sim

# collect demos
python scripts/collect_data.py \
    --task_suite_name example_suite \
    --task_name example_task \
    --robots Panda \
    --control_delta \
    --device quest

# postprocess demos
python scripts/postprocess_demos.py \
    --demo_dir ./demos/example_suite/example_task

# (optional) playback collected demos
python scripts/playback_demo.py \
    --dataset_path ./demos/example_suite/example_task/demo.hdf5 \
    --control_delta \
    --video_dir ./demos/example_suite/example_task/playback_delta/ \
    --video_skip 5 \
    --num_demos 5

######################## DATA EXPANSION USING MIMICGEN ########################

cd ../../mimicgen

# add datagen info
python scripts/prepare_src_dataset.py \
    --dataset ../data_collection/sim/demos/example_suite/example_task/demo.hdf5

# generate mimicgen configs for generating 100 demos for each task in the suite
python scripts/generate_configs_and_jobs.py \
    --task_suite_name example_suite \
    --source_demos_dir ../data_collection/sim/demos/example_suite \
    --generation_dir ../mimicgen/data/example_suite \
    --num_demos 100 \
    --camera_height 128 \
    --camera_width 128
