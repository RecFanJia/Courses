def max_sum_adjecent(s):
    """
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> max_sum_adjecent(s)
    6
    >>> s = [-4, 3, -2, -3, 2, -4]
    >>> max_sum_adjecent(s)
    1
    """
    return max([a+b for a, b in zip(s[1:], s[:-1])])