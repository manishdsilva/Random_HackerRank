#!/bin/python3

import os
import sys
import math
# Complete the solve function below.
def ncr(n,m):
    k = m-1
    return ((math.factorial(n+k))//(math.factorial(n)*math.factorial(k)))%1000000007
def solve(n, m):
    if m==0:
        return 0

    elif m==1:
        return 1
    
    else: 
        ans = ncr(n,m)
        return int(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
