from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tornet_macOS",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "requests[socks]",
    ],
    entry_points={
        "console_scripts": [
            "tornet_macos=tornet_macOS.main:main",
        ],
    },
    author="CoodeOSX",
    # macOS_addaptation="CoodeOSX",
    # adding_IPinfo="CoodeOSX",
    description="TorNet - Automate IP address changes using Tor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoodeOSX/tornet-macOS",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux :: Darwin",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.6",
    keywords="tor, anonymity, proxy, security, privacy, networking",
    project_urls={
        "Source": "https://github.com/CoodeOSX/tornet-macOS",
    },
)
