#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
print(os.getcwd())

with open('README.MD') as readme_file:
    readme = readme_file.read()
    
with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['tensorflow', 'beep', 'pandas', 'scipy', 'seaborn']

test_requirements = ['tensorflow', 'beep', 'pandas', 'scipy', 'seaborn']

setup(
    author="Mehrad Ansari",
    author_email='mehrad.ansari@rochester.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v3 License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Deep learning tool for infering battery's state of health based on cycle data.",
    entry_points={
        'console_scripts': [
            'bye_cycle=bye_cycle.cli:main',
        ],
    },
    install_requires=requirements,
    license="GPL v3 license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bye_cycle',
    name='bye_cycle',
    packages=find_packages(include=['bye_cycle', 'bye_cycle.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/TRI-AMDD/bye_cycle',
    version='0.1.0',
    zip_safe=False,
)
