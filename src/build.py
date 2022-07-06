#Must have py2exe installed.
#Run this command:
#python -m py2exe build.py

from distutils.core import setup
import tkinter, windowMain, topmenu
import py2exe

setup(console=["main.py"])