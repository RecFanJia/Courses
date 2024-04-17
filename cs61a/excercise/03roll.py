# Example usage:
def rolling_average(n):
    """
    >>> numbers = [10, 20, 30, 40, 50]
    >>> avg_gen = rolling_average(numbers)
    >>> list(avg_gen)
    [10, 15, 20, 25, 30]
    """
    total, count = 0, 0
    for x in n:
        count += 1
        total += x
        yield total // count
    