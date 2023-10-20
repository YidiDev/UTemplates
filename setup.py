from setuptools import setup, find_packages

setup(
    name="utemplates",
    version="0.21",
    packages=find_packages(),
    install_requires=[],
    author="Yidi Sprei",
    author_email="yididev@gmail.com",
    description="A Python Templating Framework to allow templating logic to be programmed in python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YidiDev/UTemplates",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
