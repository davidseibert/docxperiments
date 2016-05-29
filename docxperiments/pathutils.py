# coding: utf-8

import os
from . import PACKAGE_DIR, PROJECT_DIR, DATA_DIR, SPECIMENS_DIR, EXPERIMENTS_DIR


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def mkpath(*args):
    return os.path.join(*args)

def mkrel(path, other):
    if isinstance(path, basestring):
        return os.path.relpath(path, other)
    else:
        return [os.path.relpath(i, other) for i in path]

def project_rel(path):
    return mkrel(path, PROJECT_DIR)
def package_rel(path):
    return mkrel(path, PACKAGE_DIR)
def data_rel(path):
    return mkrel(path, DATA_DIR)
def data_abs(path):
    return mkpath(DATA_DIR, path)
def specimens_abs(path):
    return mkpath(SPECIMENS_DIR, path)
def specimens_rel(path):
    return mkrel(path, SPECIMENS_DIR)
def experiments_abs(path):
    return mkpath(EXPERIMENTS_DIR, path)
def experiments_rel(path):
    return mkrel(path, EXPERIMENTS_DIR)



def ls(root):
    ignored = {'.DS_Store'}
    def _process_level(level):
        dirpath, dirnames, filenames = level
        dirnodes = [ mkpath(dirpath, dirname) for dirname in dirnames ]
        filenodes = [ mkpath(dirpath, filename) for filename in filenames if filename not in ignored]
        return dirnodes + filenodes
    levels = os.walk(root)
    nodes = [ _process_level(level) for level in levels ]
    flattened = [subnode for subnodelist in nodes for subnode in subnodelist]
    return sorted(flattened)
