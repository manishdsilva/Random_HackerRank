#!/bin/python3

import os
import sys
from math import factorial

# Complete the solve function below.
def solve(n, m):
    result = factorial(n+m)//factorial(n)//factorial(m)%(10**9+7)
    return int(result)

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
