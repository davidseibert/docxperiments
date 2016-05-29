import difflib
from difflib import context_diff, ndiff, unified_diff 
import sys

def get_diff_battery(a_path, b_path):
    _context_diff = get_context_diff(a_path, b_path)
    _ndiff = get_ndiff(a_path, b_path)
    _unified_diff = get_unified_diff(a_path, b_path)
    return (_context_diff, _ndiff, _unified_diff)

def get_context_diff(a_path, b_path):
    a_lines = _readlines(a_path)
    b_lines = _readlines(b_path)
    diff_result_gen = context_diff(a_lines, b_lines)
    return ''.join([line for line in diff_result_gen])

def get_ndiff(a_path, b_path):
    a_lines = _readlines(a_path)
    b_lines = _readlines(b_path)
    diff_result_gen = unified_diff(a_lines, b_lines)
    return ''.join([line for line in diff_result_gen])

def get_unified_diff(a_path, b_path):
    a_lines = _readlines(a_path)
    b_lines = _readlines(b_path)
    diff_result_gen = unified_diff(a_lines, b_lines)
    return ''.join([line for line in diff_result_gen])

def _readlines(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        return lines

def main():
    a_path = '../tests/testdata/a.xml'
    b_path = '../tests/testdata/b.xml'
    #diff_result = get_diff_battery(a_path, b_path)
    diff_result = get_diff_battery(a_path, b_path)
    print diff_result


if __name__ == '__main__':
    main()
