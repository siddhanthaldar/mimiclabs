# MimicLabs Study Datasets

## Download datasets

We open-source all the datasets used in our study paper, which contains over 850k trajectories across 8 different scenes (`lab1` through `lab8`) that were used to study the effects of different retrieval strategies from a large-scale simulation dataset. We have made low-dimensional observations and actions available for download. You can add image observations to these datasets using instructions in the subsequent sub-section.

### Using web URL

You can download all datasets from [Hugging Face](https://huggingface.co/datasets/vaibhavsaxena11/mimiclabs_datasets/tree/main).

### Using provided scripts (recommended)

You can also download all datasets using the provided script (CAUTION: this will download ~323GB of data):
```bash
$ cd <PATH_TO_THIS_REPO>/mimiclabs/mimiclabs
$ python scripts/download_mimiclabs_datasets.py --download_dir <YOUR_DOWNLOAD_DIR>
```

By default the above script will download all datasets to the the download directory. You can selectively download datasets from a few labs. Below is an example command to download datasets of just `lab1` and `lab2`:
```bash
$ python scripts/download_mimiclabs_datasets.py --download_dir <YOUR_DOWNLOAD_DIR> --labs lab1 lab2
```

If you'd like to do a dry run first, run:
```bash
$ python scripts/download_mimiclabs_datasets.py --download_dir <YOUR_DOWNLOAD_DIR> --labs lab1 lab2 --dry_run
```

## Add image observations to datasets

Downloaded datasets only contain low-dim observations. To add image observations to the downloaded datasets, run:
```bash
$ cd <PATH_TO_THIS_REPO>/mimiclabs/mimiclabs
$ python scripts/add_obs_to_mimiclabs_datasets.py --input_root_dir <YOUR_DOWNLOAD_DIR>/mimiclabs_study --output_root_dir <YOUR_DOWNLOAD_DIR>/mimiclabs_study
```
This will generate a script called `add_obs_to_mimiclabs_datasets.sh` in the `scripts` directory, which you can run using:
```bash
$ chmod +x scripts/add_obs_to_mimiclabs_datasets.sh
$ ./scripts/add_obs_to_mimiclabs_datasets.sh
```
