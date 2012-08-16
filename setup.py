#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-keymanager',
    version='0.1',
    description='A simple keymanager for Django.',
    author='Erik LaBianca',
    author_email='erik.labianca@wisertogether.com',
    url='http://github.com/WiserTogether/django-keymanager/',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'django_keymanager',
    ],
    package_data={
        'tastypie': ['templates/django_keymanager/*'],
    },
    requires=[
    ],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
