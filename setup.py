import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "twitterlog",
    version = "0.0.1",
    author = "Niels Sandholt Busch",
    author_email = "niels.busch@gmail.com",
    description = ("A log handler that outputs to twitter"),
    license = "BSD",
    keywords = "twitter log",
    url = "https://bitbucket.org/resmio/twitterlog",
    modules=['twitterlog', 'tests'],
    requires=[
        'tweepy(>=1.8)'
    ],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
