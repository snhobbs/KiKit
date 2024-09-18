# -*- coding: utf-8 -*-

import setuptools
# import versioneer
import os
import sys

# Some packages on Linux for v7 change the location of the pcbnew module, let's
# add the new location to path:
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open("requirements.txt", "r") as fh:
    for line in fh.readlines():
        if not line.strip() or line.strip()[0] == "#":
            continue
        requirements.append(line.split("#")[0].strip())

setuptools.setup(
    name="KiKit",
    python_requires='>=3.7',
    version="1.0.1",#versioneer.get_version(),
    cmdclass={"class": 1},# versioneer.get_cmdclass(),
    author="Jan Mrázek",
    author_email="email@honzamrazek.cz",
    description="Automation for KiCAD boards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaqwsx/KiKit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    setup_requires=[
        "versioneer"
    ],
    extras_require={
        "dev": ["pytest"],
    },
    zip_safe=False,
    include_package_data=True,
    entry_points = {
        "console_scripts": [
            "kikit=kikit.ui:cli",
            "kikit-info=kikit.info:cli"
        ],
    }
)
