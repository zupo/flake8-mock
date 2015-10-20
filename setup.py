# coding: utf-8

from __future__ import with_statement
from setuptools import setup


def get_version(fname='flake8_mock.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-mock',
    version=get_version(),
    description="Provides checking for non-existent mock methods",
    long_description=get_long_description(),
    keywords=['flake8', 'mock', 'testing'],
    author='Alejandro Pereira',
    author_email='alepereira.dev@gmail.com',
    url='https://github.com/aleGpereira/flake8-mock',
    license='GNU',
    py_modules=['flake8_mock'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'flake8_mock = flake8_mock:MockChecker',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
