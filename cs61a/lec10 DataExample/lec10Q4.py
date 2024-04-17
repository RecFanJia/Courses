def wether_iden(s):
    """
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> wether_iden(s)
    False
    >>> s = [4, 3, 2, 3, 2, 4]
    >>> wether_iden(s)
    True
    """
    while len(s[1:]) >= 1:
        for n in s[1:]:
            if n == s[0]:
                return True
        s = s[1:]
    return False