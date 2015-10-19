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
    description="Provides checking mock non-existent methods",
    long_description=get_long_description(),
    keywords='flake8 mock',
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
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
