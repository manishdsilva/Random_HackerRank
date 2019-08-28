#!/bin/python3
from fractions import Fraction as F
import os
import sys

# Complete the solve function below.
def solve(n, k, s):
    den = n**2
    l = list(s)
    l = list(map(int,l))
    count = 0
    num = 0
    for i in range(n):
        if l[i] == 1:
            count = count + l[i]+2*sum(l[i+1:min(i+k+1,n)])
    num = num +count
    if(num==0):
        return "0/1"
    if num == den:
        return "1/1"
    return str(F(num,den))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        s = input()
        
        result = solve(n, k, s)

        fptr.write(result + '\n')

    fptr.close()
