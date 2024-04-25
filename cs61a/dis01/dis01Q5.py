def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(0) 
    1
    >>> unique_digits(8898) 
    2
    """
    unique = 0
    if n==0:
     return 1
    else:
     while n > 0:
        last = n % 10
        n = n // 10
        if not has_digit(n, last):
            unique += 1
     return unique

def has_digit(n, k):
    assert k >= 0 and k < 10
    while n > 0:
        last = n % 10
        n = n // 10
        if last == k:
            return True
    return False