
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='logmux',
    version='0.1.0',
    description='Tail multiple log files, label their lines and combine them into one stream',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/monacoremo/logmux',
    author='monacoremo',
    author_email='monacohacks@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='logs tail monitoring',
    py_modules=["logmux"],
    python_requires='>=3.7, <4',
    install_requires=['click'],
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'logmux=logmux:main',
        ],
    },
)
