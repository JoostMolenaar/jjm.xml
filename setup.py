#!/usr/bin/env python2.7

static_dirs = []
install_requires = []
tests_require = ['pytest', 'pytest-cov', 'coverage']

import os
import setuptools
import setuptools.command.test

class PyTest(setuptools.command.test.test):
    def initialize_options(self):
        setuptools.command.test.test.initialize_options(self)

    def finalize_options(self):
        setuptools.command.test.test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main('tests --cov-report html --cov-report term --cov xmlist --cov-config .coveragerc'.split())

def try_read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except: pass

setuptools.setup(
    name='xmlist',
    version=try_read_file('xmlist.egg-info/version.txt'),
    version_command=('git describe', 'pep440-git'),
    py_modules=['xmlist'],
    description='Functions for generating XML',
    author='Joost Molenaar',
    author_email='j.j.molenaar@gmail.com',
    url='http://github.com/j0057/xmlist',
    install_requires=install_requires,
    tests_require=tests_require,
    custom_metadata={
        'x_static_dirs': static_dirs
    },
    data_files=[ (root, [ root + '/' + fn for fn in files ])
                 for src_dir in static_dirs
                 for (root, dirs, files) in os.walk(src_dir) ],
    cmdclass = { 'test': PyTest })
