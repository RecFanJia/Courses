# Example usage:
def gen_primes():
    """
    >>> primes = gen_primes()
    >>> [next(primes) for _ in range(5)]
    [2, 3, 5, 7, 11]
    """
    def is_prime(x):
        count=0
        for k in range(1,x+1):
            if x%k==0:
                count+=1
        return True if count==2 else False 
    n=2
    while True:
        if is_prime(n):
            yield n
        n+=1