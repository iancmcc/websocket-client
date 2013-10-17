import os
from setuptools import setup, find_packages
from distutils.core import Extension


VERSION = "0.11.1"


setup(
    name="websocket-client",
    version=VERSION,
    description="WebSocket client for python. hybi13 is supported.",
    long_description=open("README.rst").read(),
    author="liris",
    author_email="liris.pp@gmail.com",
    license="LGPL",
    url="https://github.com/liris/websocket-client",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    keywords='websockets',
    scripts=["bin/wsdump.py"],
    packages=find_packages('src'),
    package_dir={'':'src'},
    ext_modules=[Extension('websocket._mask', ['src/websocket/_mask.c']),
                 Extension('websocket._fastmask', ['src/websocket/_fastmask.c'])]
)
