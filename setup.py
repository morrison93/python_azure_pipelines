# setup.py
from setuptools import setup, find_packages

setup(
    name='flask_app',
    version = '0.1.7', #TODO : NE pas oubliez de changer la version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[line.strip() for line in open("requirements.txt",encoding="utf-8").readlines()],
    setup_requires=[
        'setuptools>=57.4.0',
    ],
)