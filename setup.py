#!/usr/bin/env python
from setuptools import find_packages, setup


def get_long_description():
    with open('README.rst') as f:
        return f.read()


setup(
    name='stix2-generator',
    version='0.2.0',
    description='Generate random STIX 2 content.',
    long_description=get_long_description(),
    long_description_content_type='text/x-rst',
    url='https://github.com/oasis-open/cti-stix-generator',
    author='OASIS Cyber Threat Intelligence Technical Committee',
    author_email='cti-users@lists.oasis-open.org',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='stix stix2 json generator generation stix2-generator',
    packages=find_packages(exclude=['*.test', '*.test.*']),

    python_requires='>= 3.7',

    install_requires=[
        'Faker',
        'lark-parser',
        'pytz',
        'stix2 >= 3.0.0'
    ],

    extras_require={
        'jupyter': ['jupyter', 'stix2-viz'],
        'tests': ['pytest', 'rdflib']
    },

    package_data={
        'stix2generator': ['stix21_registry.json']
    },

    entry_points={
        'console_scripts': [
            'build_stix = stix2generator.language.build_stix:main',
            'generate_stix = stix2generator.generation.generate_stix:main'
        ]
    }
)
