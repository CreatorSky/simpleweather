import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpleweather",
    version="0.0.1",
    author="Akash Parmar",
    author_email="akashparmar@outlook.in",
    description="A simple weather module for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/creatorsky/simpleweather",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)