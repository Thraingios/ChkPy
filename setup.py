'''
Author(s): Nick
Created date: 12/3/21
Description: sets up for pip installation
last edit: 12/3/21
'''

import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Wrapper for 3 python tools to aid in code development'

# Setting up
setup(
    name="chkpy",
    version=VERSION,
    author="Anthony Clark, Dylan Haus & Nick Cardin",
    author_email="<mail@unh.edu>",
    long_description=long_description,
    license='GPLv3',
    description=DESCRIPTION,
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
