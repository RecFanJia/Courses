# Example usage:
def fibonacci():
    """
    >>> fib = fibonacci()
    >>> [next(fib) for _ in range(10)]  # Should output the first 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    before,after=0,1
    while True:
        yield before
        before,after=after,before+after   