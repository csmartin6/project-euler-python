from distutils.core import setup
import sys

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

setup(
    name='project_euler',
    version='0.3.0',
    packages=['project_euler'],
    url='',
    license='',
    author='Chris Martin',
    author_email='cmartin@palantir.com',
    description='Project Euler Solutions',
    tests_require=['pytest','pytest-benchmark'],
    cmdclass = {'test': PyTest}
)
