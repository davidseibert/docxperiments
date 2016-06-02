def group(n=None):
    if isinstance(n, int):
        return r'\g<{}>'.format(n)
    else:
        return r'({})'.format(n)


def run_property(property):
    return _rPr[0] + property + _rPr[1]

