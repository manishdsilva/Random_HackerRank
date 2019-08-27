#!/bin/python3

import os
import sys
import math
#
# Complete the divisors function below.
#
def divisors(n):
    #
    # Write your code here.
    product = 0
    flag = 1
    while(n//2 >0 and (n%2)==0):
        n = n/2
        product += 1
    ct = 0
    for i in range(3,int(math.sqrt(n))+1,2):
        product = product*(ct+1)
        ct = 0
        while(n%i==0):
            n = n/i
            ct = ct + 1
    if ct != 0 :
        product = product*(ct+1)
    if n > 2:
        flag = 2
    
    return flag*product

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
