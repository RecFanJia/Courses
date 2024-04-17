def map_d(s):
    """
    >>> s = [5, 8, 13, 21, 34, 55, 89]
    >>> map_d(s)
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    dic = {}
    for n in s:
        if n%10 in dic.keys():
            dic[n % 10].append(n)
        else:
            dic[n % 10] = [n]
    return dict(sorted(dic.items()))