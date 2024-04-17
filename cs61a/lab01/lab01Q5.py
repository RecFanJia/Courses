def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    
    up,sum,ex=y,0,10
    while ex//10 <=up:
      sum=sum+(y%ex)//(ex//10)
      y=y-y%ex
      ex=ex*10
    return sum

  #total = 0
    #while y > 0:
        #total, y = total + y % 10, y // 10
    #return total
#the solution eleminate 1 digit everytime, instead of changing digit to 0 after each calculation