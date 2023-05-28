from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ech0_mind",
    version="0.1",
    packages=["ech0_mind"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ech0=ech0_mind.cli.main:app",
        ],
    },
)
