import os
from setuptools import setup, find_packages


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

long_description = read_file('README.md')
license_text = read_file('LICENSE').strip()

setup(
    name="crxsnake",
    version="1.3.0",
    description="A collection of functions for creating Discord bots.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://discord.gg/EEp67FWQDP",
    author="CRX-DEV",
    author_email="cherniq66@gmail.com",
    license=license_text,
    packages=find_packages(include=["crxsnake", "crxsnake.*"]),
    install_requires=[
        "tortoise-orm==0.21.0",
        "disnake==2.9.2",
        "aiofiles==23.2.1",
        "loguru==0.7.2",
    ],
)
