def generate_binary_strings(n):
    """
    A generator function that yields all binary strings of length n.

    >>> list(generate_binary_strings(2))
    ['00', '01', '10', '11']
    """

    if n==0:
        yield ""
    elif n==1:
        yield "0"
        yield "1"
    else:
        for x in generate_binary_strings(n-1):
            yield x+"0"
            yield x+"1"