#Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


# Input Format
# A single line containing a positive integer, .


# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input :- 3
# Sample Output :- Weird

# Explanation 
# is odd and odd numbers are weird, so print Weird.

# Sample Input:- 24
# Sample Output:- Not Weird
# Explanation 
# n=24 ,n>20 and  is even, so it is not weird.


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
  n = int(input().strip())
  check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])
    