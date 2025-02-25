from setuptools import setup, find_packages

setup(
    name='L',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'L=Compile.main:main',
        ],
    },
    author='Lakshit Upreti',
    description='A programming language for fun',
)