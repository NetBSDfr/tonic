import os
from setuptools import setup

setup(
    name = "Tonic",
    version = "0.1-dev",
    author = ["Guillaume Delpierre", "Sylvain Mora"],
    author_email = ["gde@llew.me", "sylvain.mora@solevis.net"],
    description = ("A simple GUI for pkgin."),
    license = "BSD",
    keywords = "package manager gui pkgin tonic pkgsrc",
    url = "http://tonic.pkgin.net/",
    packages = ['tonic', 'tonic/widgets'],
    scripts = ["./tonic-client"],
    long_description = "Tonic is a GUI written with wxWidget to "\
                       "manage binary package from pkgsrc using "\
                       "pykgin as backend for pkgin",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python",
    ],
)
