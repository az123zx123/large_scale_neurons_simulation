# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:45:50 2020

@author: li xiang
"""

import sys
from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32": 
    base = "Win32GUI"
setup( name = "neuronsimulation", 
       version = "0.1", 
       description = "neurons simulation", 
       options = {"build_exe": build_exe_options}, 
       executables = [Executable("guifoo.py", base=base)]
)