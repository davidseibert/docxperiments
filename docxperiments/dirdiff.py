# coding: utf-8

import os, filecmp
from pathutils import ls

# This needs to be deleted, but my test depends on it...
def walk_dir(root):
    return ls(root)

def get_left_only(a_path, b_path):
    a_nodes = walk_dir(a_path)
    b_nodes = walk_dir(b_path)
    a_std = _standardize(a_nodes, a_path)
    b_std = _standardize(b_nodes, b_path)
    a_minus_b = [ node for node in a_std if node not in b_std ]
    return a_minus_b
 
def get_right_only(a_path, b_path):
    a_nodes = walk_dir(a_path)
    b_nodes = walk_dir(b_path)
    a_std = _standardize(a_nodes, a_path)
    b_std = _standardize(b_nodes, b_path)
    b_minus_a = [ node for node in b_std if node not in a_std ]
    return b_minus_a
    
def get_common(a_path, b_path):
    a_nodes = walk_dir(a_path)
    b_nodes = walk_dir(b_path)
    a_std = _standardize(a_nodes, a_path)
    b_std = _standardize(b_nodes, b_path)
    b_and_a = [ node for node in b_std if node in a_std ]
    return b_and_a

def _standardize(nodes, parent):
    std = [ os.path.relpath(node, parent) for node in nodes ]
    return std


def main():
    pass

if __name__ == '__main__':
    main()