# setup.py
from setuptools import setup, find_packages

setup(
    name="kali_exploit_tools",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "requests",
        "python-nmap"       # Nmap integration for Python
    ],
    entry_points={
        "console_scripts": [
            "kali-exploit-tools=main:run"
        ]
    },
    include_package_data=True,
    description="A Python 3 package for network exploitation tools like Nmap, SQLMap, and BeEF functionalities.",
    author="Mark Nations",
    license="MIT",
)
