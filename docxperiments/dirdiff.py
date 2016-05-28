# coding: utf-8

import os, filecmp

def _process_level(root, level, no):
    subnodes = []
    root_name = os.path.basename(root)
    dirpath, dirnames, filenames = level
    subroot = os.path.basename(dirpath)
    for dirname in dirnames:
        subnodes.append(os.path.join(dirpath, dirname))
    for filename in filenames:
        subnodes.append(os.path.join(dirpath, filename))
    return subnodes

def walk_dir(root):
    ignored = set()
    ignored.add('.DS_Store')

    head, tail = os.path.split(root)
    levels = os.walk(root)

    nodes = []
    i = 0
    for no, level in enumerate(levels):
        subnodes = _process_level(root, level, no)
        nodes.append(subnodes)
        i += 1

    flattened = [subnode for subnodelist in nodes for subnode in subnodelist]

    return [os.path.relpath(node, head) for node in sorted(flattened) if os.path.basename(node) not in ignored ]

def get_left_only(a_path, b_path):
    a_nodes = walk_dir(a_path)
    b_nodes = walk_dir(b_path)
    a_std = [
        '/'.join(
            node.split('/')[1:]
            ) for node in a_nodes ]
    b_std = [
        '/'.join(
            node.split('/')[1:]
            ) for node in b_nodes ]
    a_minus_b = [ node for node in a_std if node not in b_std ]
    return a_minus_b
 
def get_right_only(a_path, b_path):
    a_nodes = walk_dir(a_path)
    b_nodes = walk_dir(b_path)
    a_std = ['/'.join(node.split('/')[1:]) for node in a_nodes ]
    b_std = ['/'.join(node.split('/')[1:]) for node in b_nodes ]
    b_minus_a = [ node for node in b_std if node not in a_std ]
    return b_minus_a
    
def get_common(a_path, b_path):
    a_nodes = walk_dir(a_path)
    b_nodes = walk_dir(b_path)
    a_std = ['/'.join(node.split('/')[1:]) for node in a_nodes ]
    b_std = ['/'.join(node.split('/')[1:]) for node in b_nodes ]
    b_and_a = [ node for node in b_std if node in a_std ]
    return b_and_a

def main():
    pass

if __name__ == '__main__':
    main()