from setuptools import setup

with open('requirements.txt') as f:
    packages = f.read().splitlines()

setup(
    name="imdb-sentiment-analysis",
    version="1.0",
    description="_",
    author="Modojojo",
    install_requires=packages
)