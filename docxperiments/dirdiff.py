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
    return []
def get_right_only(a_path, b_path):
    return []
def get_common(a_path, b_path):
    return []


def main():
    a_path = '../tests/testdata/diffsampleA'
    b_path = '../tests/testdata/diffsampleB'
    a_nodes = walk_dir(a_path)
    a_list_str = '\n'.join(a_nodes)
    print a_list_str
    b_nodes = walk_dir(b_path)
    b_list_str = '\n'.join(b_nodes)
    print b_list_str

    print '\n A\n---'
    a_std = [
        '/'.join(
            node.split('/')[1:]
            ) for node in a_nodes ]
    print '\n'.join(a_std)

    print '\n B\n---'
    b_std = [
        '/'.join(
            node.split('/')[1:]
            ) for node in b_nodes ]
    print '\n'.join(b_std)

    print '\n A - B\n-------'
    a_minus_b = [ node for node in a_std if node not in b_std ]
    print '\n'.join(a_minus_b)

    print '\n B - A\n-------'
    b_minus_a = [ node for node in b_std if node not in a_std ]
    print '\n'.join(b_minus_a)

    print '\n A x B\n-------'
    b_minus_a = [ node for node in b_std if node in a_std ]
    print '\n'.join(b_minus_a)

if __name__ == '__main__':
    main()
