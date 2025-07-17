"""
Script to download MimicLabs assets from Google Drive.
Note that the current assets directory will be removed if it exists.

Example usage:
    python scripts/download_mimiclabs_assets.py
"""

import os
import shutil
import gdown

from mimiclabs.mimiclabs import assets_root as ASSETS_ROOT


ASSETS_URLs = {
    "assets.zip": "https://drive.google.com/file/d/1YPJWR8rtPR0NLp9W2G-qYDUH6F7uXU2l/view?usp=sharing"
}


def download_file_from_gdrive(url, download_dir, dst_filename):
    """
    Download a file from Google Drive using gdown.
    """
    tmp_dir = os.path.join(download_dir, "tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    # Download file
    curr_dir = os.getcwd()
    os.chdir(tmp_dir)
    print(f"Downloading {url} to {tmp_dir}")
    gdown.download(url, tmp_dir, quiet=False, fuzzy=True)
    tmp_fname = os.listdir(tmp_dir)[0]
    tmp_path = os.path.join(tmp_dir, tmp_fname)
    os.chdir(curr_dir)

    # Move downloaded file to destination
    dst_path = os.path.join(download_dir, dst_filename)
    if os.path.exists(dst_path):
        inp = input(
            f"File {dst_path} already exists. Would you like to overwrite it? y/n\n"
        )
        if inp.lower() in ["y", "yes"]:
            shutil.move(tmp_path, dst_path)
        else:
            print(f"File {dst_path} not overwritten.")
    else:
        shutil.move(tmp_path, dst_path)
    shutil.rmtree(tmp_dir)


def download_mimiclabs_assets():
    """
    Download the MimicLabs assets from Google Drive.
    """
    download_dir = ASSETS_ROOT
    if os.path.exists(download_dir):
        print(
            f"Warning: Directory {download_dir} already exists. Removing in favour of new assets that will be downloaded."
        )
        shutil.rmtree(download_dir)
    os.makedirs(download_dir, exist_ok=True)

    # Download each file
    for filename, url in ASSETS_URLs.items():
        assert filename.endswith(".zip"), f"File {filename} is not a zip file."

        # Download file
        download_file_from_gdrive(url, download_dir, filename)  # TEMP disable
        # Unzip files if necessary
        if filename.endswith(".zip"):
            zip_path = os.path.join(download_dir, filename)
            shutil.unpack_archive(zip_path, download_dir)
            os.remove(zip_path)
            # Move contents of the unzipped folder to the download directory
            # and remove the unzipped folder
            unzipped_folder = os.path.join(download_dir, filename[:-4])
            for item in os.listdir(unzipped_folder):
                item_path = os.path.join(unzipped_folder, item)
                if os.path.isdir(item_path):
                    shutil.move(item_path, download_dir)
                else:
                    shutil.move(item_path, os.path.join(download_dir, item))
            shutil.rmtree(unzipped_folder)
    print(f"Assets downloaded to {download_dir}")


if __name__ == "__main__":
    download_mimiclabs_assets()
