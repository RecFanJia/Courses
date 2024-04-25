def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    k=2  
    if n==1:
     return False
    else:
     while n>=k:
      if n %k ==0 and n != k:
         return False
      k +=1
      return True
    