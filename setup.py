# To use a consistent encoding
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyzu',
    version='0.1',
    description='Library to work with Open Graph metadata',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/chason/pyzu',
    author='Chason Chaffin',
    author_email='chason@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='opengraph opengraph-data rdfa rdflib',
    py_modules=["pyzu"],
    install_requires=['requests', 'rdflib'],
    extras_require={
        'dev': ['bumpversion'],
        'test': [
            'pytest',
            'coverage',
            'python-coveralls',
            'pytest-cov',
        ],
    },
    python_requires='>=3.6',
)
