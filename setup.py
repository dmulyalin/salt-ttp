from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

__author__ = "Denis Mulyalin <d.mulyalin@gmail.com>"

setup(
    name="salt_ttp",
    version="0.1.0",
    author="Denis Mulyalin",
    author_email="d.mulyalin@gmail.com",
    description="SALTSTACK TTP Modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmulyalin/salt-ttp",
    packages=find_packages(),
    include_package_data=True,
    data_files=[('', ['LICENSE'])],
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points = """
	[salt.loader]
    module_dirs=salt_ttp.loader:module_dirs	
	runner_dirs=salt_ttp.loader:runner_dirs	
	"""
)
