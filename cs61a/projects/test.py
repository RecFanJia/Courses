def remove(n, digit):
    """
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits=0, 0
    while n>0:
        last, n= n%10, n//10
        #n, last= n//10, n%10
        if last!=digit:
           kept= last*10**digits+kept
           digits= digits+1
    return kept