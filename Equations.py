#!/bin/python3

import os
import sys
import math

def expFactor(n, p): 
    x = p 
    exponent = 0
    while n // x > 0: 
      
        exponent += n // x 
        x *= p 
    return exponent 
  
# Returns the no  
# of factors in n! 
def divisors(n): 
  
    # ans stores the no 
    # of factors in n! 
    ans = 1
  
    # Find all primes upto n 
    prime = [None]*(n+1) 
      
    # Initialize all 
    # numbers as prime 
    for i in range(1,n+1): 
        prime[i] = 1
  
    # Mark composites 
    prime[1] = 0
    i = 2
    while i * i <= n: 
      
        if (prime[i]): 
          
            for j in range(i * i,n+1,i): 
                prime[j] = 0
        i += 1
  
    # Multiply exponent (of 
    # primes) added with 1 
    for p in range(1,n+1): 
      
        # if p is a prime then p  
        # is also a prime factor of n! 
        if (prime[p] == 1): 
            ans *= (2*expFactor(n, p) + 1) 
  
    return ans 

def solve(n):
    return (divisors(n))%1000007
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
