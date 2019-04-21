# !/usr/bin/env python
import setuptools
from distutils.core import setup


tests_require = [
    'cookiecutter>=1.4.0',
    'pytest',
    'pytest-cookies',
    'tox',
]

docs_require = [
    'Sphinx',
    'sphinx_rtd_theme',
]

setup(
    name='cuppy-cookiecutter',
    packages=[],
    version='0.0.1',
    description='Cookiecutter template for Cuppy addons',
    author='Cuppy developers',
    license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
    author_email='ephraimanierobi@gmail.com',
    url='https://github.com/ephraimbuddy/cuppy-cookiecutter',
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    extras_require={
        'docs': docs_require,
        'tests': tests_require,
        },
)