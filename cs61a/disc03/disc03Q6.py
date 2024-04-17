# write any code you want
from karel.stanfordkarel import *

def main():
   if front_is_clear():
      if front_is_clear():
         move()
         if front_is_clear():
            move()
         else:
            turn_left()
            turn_left()
         if front_is_clear():
            turn_left()
            if front_is_clear():
               turn_left()
               turn_left()
               turn_left()
               main()
            else:
               turn_left()
               turn_left()
               turn_left()
      move() 