import sys
from os import path
sys.path.append(
    path.dirname( # PROJECT
    path.dirname( # PACKAGE
    path.dirname( # PACKAGE/synthesis
    path.abspath(__file__))))) # PACKAGE/synthesis/context.py
