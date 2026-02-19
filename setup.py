from setuptools import setup, find_packages

setup(
    name="gecko",
    version="1.0.0",
    description="A lightweight, open-source personal AI agent.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="OpenClaw AI Assistant",
    author_email="openclawster@gmail.com",
    url="https://github.com/openclawster/gecko",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "gecko=__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
