def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total=1
    m=n-k
    while n>m:
      total=total*n
      n=n-1
    return total



#after combining of lines
    #total, stop = 1, n-k
    #while n > stop:
    #    total, n = total*n, n-1
    #return total

