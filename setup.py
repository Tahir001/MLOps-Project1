from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "MLOPS-Project-1",
    version="0.1", 
    author="Tahir Muhammad", 
    packages = find_packages(), # Automatically detect all of the packages (Custom aswell i.e. src, utils, etc)
    install_requires = requirements
)
