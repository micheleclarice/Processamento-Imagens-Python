from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="forca_python",
    version="0.0.1",
    author="Gustavo Tavares",
    description="Pacotes forca em python",
    url="https://github.com/Tavares264/Pacotes_Python",
    packages=find_packages(),
    install_requires=requirements,
)