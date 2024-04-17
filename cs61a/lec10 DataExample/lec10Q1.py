def indices_smallest(s):
    """
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> indices_smallest(s)
    [2, 4]
    >>> s = [1, 2, 3, 4, 5]
    >>> indices_smallest(s)
    [0]
    """
    indices =[] 
    smallest = min( map( abs, s))
    for i in range(len(s)):
        if abs(s[i]) == smallest:
            indices.append(i)
    return indices