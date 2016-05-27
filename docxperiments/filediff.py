
ham = [
    'The ten-dollar',
    'founding father without a father',
    'got a lot farther'
    'by working a lot harder',
    'by being a lot smarter',
    'by being a self-starter',
    'by fourteen, they placed him in charge of a trading charter.',
    ]

import difflib
from difflib import context_diff, ndiff, unified_diff, 

def check_diff(a, b):
    diff_result = difflib.context_diff(a, b)
    return diff_result
    
def run_diff_battery(a, b):
    pass


def main():
    for line in difflib.context_diff(
        [ham[0]], [ham[1]]):
        print line
    for line in difflib.unified_diff(
        [ham[0]], [ham[1]]):
        print line
if __name__ == '__main__':
    main()