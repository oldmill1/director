#!/usr/bin/env python3
"""
Setup script for Producer package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="producer",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for automating terminal and coding video creation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/producer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "producer=producer.main:main",
        ],
    },
    install_requires=[
        # Add your dependencies here if any
    ],
)
