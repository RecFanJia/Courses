def permute_string(s):
    """
    A generator function that yields all permutations of string s.

    >>> sorted(list(permute_string('ab')))
    ['ab', 'ba']
    """
    if len(s)==1:
        yield str(s)
    else:
        for x in permute_string(s[1:]):
            yield s[0]+x
            yield x+s[0]