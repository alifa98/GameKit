from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="gameTheory",
    version="0.0.11b", # change manually, create the tag and push it to github
    description="A library for Game Theory",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/alifa98/GameKit",
    author="Ali Faraji",
    author_email="ali@faraji.info",
    license="GPLv3",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.9",
    package_data={"": ["LICENSE"]},
)