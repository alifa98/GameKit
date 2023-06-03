from setuptools import setup, find_packages
import subprocess
import os

# This function gets the tag name from the last successful git tag push
def get_version():
    try:
        version = (
            subprocess.check_output(["git", "describe", "--tags"])
            .decode("utf-8")
            .strip()
        )
        if version.startswith("v"):
            version = version[1:]
        return version
    except Exception:
        return "0.0.0"

setup(
    name="gameTheory",
    version=get_version(),
    description="A library for Game Theory",
    url="https://github.com/alifa98/GameKit",
    author="Ali Faraji",
    author_email="ali@faraji.info",
    license="GPLv3",
    packages=find_packages(exclude=["gamekit*.tests.*", "tests.*"]),
    include_package_data=True,
    install_requires=[
        "pytest~=7.1.2",
        "setuptools~=63.1.0"
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.8",
    package_data={"": ["LICENSE"]},
)