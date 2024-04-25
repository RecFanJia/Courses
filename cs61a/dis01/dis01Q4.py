def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    
    while n>=1:
      if n%10==k:
       return True
      n = n//10
    return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    i=0
    count=0
    while i<10:
     if has_digit(n,i)==True:
        count += 1
     i+=1 
    return(count)     

#https://cs61a.org/disc/sol-disc01/
# ==True is redundant
# order of def doesnt matter in python