def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def count_divisors(n, i=1):
        if i > n:  
           return 0
        else:
           return (n % i == 0) + count_divisors(n, i + 1)
    return count_divisors(n)==2
    