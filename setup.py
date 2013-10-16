import os
from setuptools import setup
from distutils.core import Extension


VERSION = "0.11.0"


def extensions():
    root = os.path.dirname(__file__)
    for dpath, dnames, fnames in os.walk(root):
        fqdn = '.'.join(dpath.replace(root, '').lstrip('/').split('/'))
        for fname in fnames:
            if fname.endswith('.c'):
                yield Extension('%s.%s' % (fqdn, fname[:-2]), 
                        ['%s/%s' % (dpath, fname)])


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
    py_modules=["websocket"],
    scripts=["bin/wsdump.py"],
    ext_modules=list(extensions())
)
