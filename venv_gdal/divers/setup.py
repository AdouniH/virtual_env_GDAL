# -*- coding: utf-8 -*-
"""
Created on Sat May  5 18:10:21 2018

@author: houssem
"""

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["shapely", "fiona","matplotlib","enum"], "excludes": []}

setup(
      name = "nom",
      version = "1.0",
      description = "blablabla",
      options = {"build_exe": build_exe_options},
      executables = [Executable("app.py")]
)