#!/bin/python3

import os
import sys
import math

# Complete the solve function below.

def solve(n):
    n = n+1
    b = []
    C = 1 
    for i in range(1, n + 1):  
        b.append(int(C)%(10**9))
        C = int(C * (n - i) // i)  
    return b  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
