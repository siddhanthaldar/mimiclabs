from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "./README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="mimiclabs",
    packages=[package for package in find_packages() if package.startswith("mimiclabs")],
    install_requires=[],
    eager_resources=["*"],
    include_package_data=True,
    python_requires=">=3",
    description="MimicLabs",
    author="Vaibhav Saxena, Matthew Bronars, Nadun Ranawaka, Kuancheng Wang, Woo Chul Shin, Soroush Nasiriany, Ajay Mandlekar, Danfei Xu",
    author_email="vsaxena33@gatech.edu",
    version="1.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
