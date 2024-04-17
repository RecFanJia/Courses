def gcd(a,b):
    """
    >>> a=12
    >>> b=48
    >>> gcd(a,b)
    12
    >>> a=495
    >>> b=385
    >>> gcd(a,b)
    55
    """
    if a == b:
        return a
    else:
        return gcd(min(a,b),abs(a-b))
