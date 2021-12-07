'''
Author(s): Nick, Dylan
Created date: 12/3/21
Description: sets up for pip installation
last edit: 12/6/21
'''

import os
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


# Setting up
setup(
    name="chkpy",
    version= '1.0.0',
    author="Anthony Clark, Dylan Haus & Nick Cardin",
    author_email="<mail@unh.edu>",
    description='Wrapper for 3 python tools to aid in code development',
    long_description='File: README.md',
    license='GPLv3',
    long_description_content_type="text/markdown",
    url="https://github.com/nwc1020/ChkPy",
    packages=['chkpy'],
    install_requires=['autopep8', 'pylint'],
    keywords=['python', 'wrapper', 'development'],
    entry_points={'console_scripts': ['chkpy = chkpy.__main__:main']},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ]
)
