import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_lib_pkg",
    version="0.0.1",
    author="KIVIDARK",
    author_email="kividak@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KIVIDARK/Lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: SS License",
        "Operating System :: OS Independent",
    ],
)
