#Must have py2exe installed.'
#Run this program to build for Windows (Unix not tested.)

from distutils.core import setup
import py2exe

setup(console=["main.py"])