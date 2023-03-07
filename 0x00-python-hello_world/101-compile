#!/usr/bin/python3
import py_compile
import os

pyfile = os.environ.get('PYFILE')
if pyfile:
    py_compile.compile(pyfile, cfile=f"{pyfile}c")
else:
    print("Error: PYFILE environment variable not set.")
