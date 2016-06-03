# coding: utf-8

import os

def mkpath(*args):
    return os.path.join(*args)

ANALYSIS_DIR = mkpath(os.path.dirname(__file__))
PACKAGE_DIR = mkpath(os.path.dirname(ANALYSIS_DIR))
PROJECT_DIR = mkpath(os.path.dirname(PACKAGE_DIR))
DATA_DIR = mkpath(ANALYSIS_DIR, 'data')
TESTS_DIR = mkpath(PROJECT_DIR, 'tests')
TESTDATA_DIR = mkpath(TESTS_DIR, 'testdata')
SPECIMENS_DIR = mkpath(DATA_DIR, 'specimens')
EXPERIMENTS_DIR = mkpath(DATA_DIR, 'experiments')


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


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



def ls(root, depth=None):
    ignored = {'.DS_Store'}

    levels = os.walk(root)

    nodes = []
    for n, level in enumerate(levels):
        if depth is not None and n > depth:
            break
        dirpath, dirnames, filenames = level
        dirnodes = [ mkpath(dirpath, dirname) for dirname in dirnames ]
        filenodes = [ mkpath(dirpath, filename) for filename in filenames if filename not in ignored]
        nodes.append(dirnodes + filenodes)

    flattened = [subnode for subnodelist in nodes for subnode in subnodelist]
    return sorted(flattened)
