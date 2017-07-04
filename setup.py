from setuptools import setup, find_packages

setup(
    name="wei-dev",
    version="0.2.0",
    packages=find_packages(),
    description="DevTool for weichat development and testing, "
                "GUI and CLI tool and testing util-library included.",
    install_requires=(
        "cmdtree",
        "requests",
    ),
)
