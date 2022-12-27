from setuptools import setup
# py setup.py bdist_wheel
# twine upload dist/*
class MODULE:
    NAME = 'icantech'
    VERSION = '1.0.4'
    URL = 'https://github.com/GE-Teacher/icantech-pythonlib'
    LICENSE = 'MIT License'
    DESCRIPTION = 'Python library for ICANTECH'

class AUTHOR:
    NAME = 'hlight'
    EMAIL = 'tqh.workmail@gmail.com'


setup(
    name=MODULE.NAME,
    version=MODULE.VERSION,
    url=MODULE.URL,
    license=MODULE.LICENSE,
    author=AUTHOR.NAME,
    author_email=AUTHOR.EMAIL,
    description=MODULE.DESCRIPTION,
    packages=[
        'icantech',
        'icantech.replit',
        'icantech.replit.unittest'
    ],
    package_data={
        'icantech':['*.pyi'],
        'icantech.replit': ['*.pyi'],
        'icantech.replit.unittest': ['*.pyi']
    },
    include_package_data = True,
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    requires=[
        "inspect",
        "ast",
        "multiprocessing"
    ]
)
