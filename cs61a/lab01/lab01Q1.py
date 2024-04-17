def xk(c, d):
    """
    >>> xk(10, 10)
    23
    >>> xk(10, 6)
    23
    >>> xk(4, 6)
    6
    >>> xk(0, 0)
    25
    """
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25
    
def how_big(x):
  """
  >>> how_big(7)      
  'big'

  >>> print(how_big(7)) 
  big

  >>> how_big(12)
  huge
  positive
  >>> print(how_big(12))
  huge
  positive
  None
  >>> print(how_big(1), how_big(0))
  positive
  0
  None None
  """
  if x > 10:
    print('huge')
  elif x > 5:
    return 'big'
  if x > 0:
    print('positive')
  else:
        print(0)

n = 3
while n >= 0:
  n -= 1
  print(n)
"""
2
1
0
-1
"""

negative = -12
while negative:
  if negative + 6:
    print(negative)
    negative += 3
"""
-12
-9
"""