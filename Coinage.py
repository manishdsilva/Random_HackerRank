#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, coins):
    result = 0

    for j in range(min(coins[1]+1,500)):
        for k in range(min(coins[2]+1,200)):
            if(j*2+k*5> n):
                break
            for l in range(min(coins[3]+1,100)):
                if(j*2+k*5+l*10 > n):
                    break
                elif(j*2+k*5+l*10 in range(n-coins[0],n+1)):
                    result += 1
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        coins = list(map(int, input().rstrip().split()))

        result = solve(n, coins)

        fptr.write(str(result) + '\n')

    fptr.close()
