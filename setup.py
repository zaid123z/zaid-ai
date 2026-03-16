# Project Configuration

# This is the setup script for the zaid-ai project.

from setuptools import setup, find_packages

setup(
    name='zaid-ai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
    ],
    entry_points={
        'console_scripts': [
            'zaid-ai=zaid_ai:main',  # Adjust according to your main module
        ],
    },
    # Other configuration options
)