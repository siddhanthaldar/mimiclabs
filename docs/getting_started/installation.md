# Installation

### 1. Setting up your conda environment
```bash
$ conda create -n mimiclabs python=3.10
$ conda activate mimiclabs
```

### 2. Installing supporting libraries
Run the following commands to install **Robosuite**, **LIBERO**, **MimicGen**, and **RoboCasa**.
```bash
# install LIBERO
(mimiclabs)$ git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
(mimiclabs)$ cd LIBERO
(mimiclabs)$ pip install -e .
(mimiclabs)$ cd ..

# install MimicGen
(mimiclabs)$ git clone https://github.com/NVlabs/mimicgen.git
(mimiclabs)$ cd mimicgen
(mimiclabs)$ pip install -e .
(mimiclabs)$ cd ..

# (optional) install RoboCasa (for additional assets)
(mimiclabs)$ git clone https://github.com/robocasa/robocasa.git
(mimiclabs)$ cd robocasa
(mimiclabs)$ pip install -e .
# next: follow instructions on their github to download robocasa assets
(mimiclabs)$ cd ..

# install Robomimic
(mimiclabs)$ git clone https://github.com/ARISE-Initiative/robomimic.git
(mimiclabs)$ cd robomimic
(mimiclabs)$ pip install -e .
(mimiclabs)$ cd ..

# install Robosuite
(mimiclabs)$ git clone https://github.com/ARISE-Initiative/robosuite.git
(mimiclabs)$ cd robosuite && git checkout b9d8d3de5e3dfd1724f4a0e6555246c460407daa
(mimiclabs)$ pip install -e .
(mimiclabs)$ cd ..
```

<div class="admonition note">
    <p class="admonition-title">Note: Cannot import RoboCasa</p>
    You might not be able to import robocasa due to robosuite version mismatch. This is completely fine as we'll only require robocasa for assets.
</div>


### 3. Installing MimicLabs
```bash
(mimiclabs)$ git clone <link_to_this_repo>
(mimiclabs)$ cd mimiclabs
(mimiclabs)$ pip install -e .
(mimiclabs)$ pip install -r requirements.txt
```

<div class="admonition warning">
    <p class="admonition-title">Warning: Check MuJoCo version</p>
    Make sure you have mujoco==3.1.1 installed. Later versions might throw errors when initializing certain scenes. 
</div>

### 4. Downloading MimicLabs assets
```bash
(mimiclabs)$ cd mimiclabs/mimiclabs
(mimiclabs)$ python scripts/download_mimiclabs_assets.py
```
