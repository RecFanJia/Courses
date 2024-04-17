def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself.
    >>> num_factors(21)
    4
    """
    # BEGIN PROBLEM 4
    i,n_f=1,0
    while n>=i:
     if n%i==0:
      n_f+=1
     i+=1
    return n_f

    # END PROBLEM 4

def sus_points(n):
    """Return the new score of a player taking into account the Sus Fuss rule.
    >>> sus_points(21)
    23
    """
    # BEGIN PROBLEM 4
    if num_factors(n) == 3 or num_factors(n) == 4:
        while not is_prime(n): 
          n += 1
    return n