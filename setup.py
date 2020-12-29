import setuptools
import json

with open("setup.json", "r") as f:
    data = json.load(f)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=data['name'], # Replace with your own username
    version=data['version'],
    author=data['author'],
    author_email=data['author_email'],
    description=data['description'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=data['url'],
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where='src',exclude=("test")),
    package_data={"sshcmds":["runcmds.json"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=data['python_version'],
    entry_points={
        "console_scripts": [
            "sshcli = sshcmds.sshcli:main",
        ]
    }
    
)