#!/bin/python3

import os
import sys

#
# Complete the strangeGrid function below.
#
even = [0,2,4,6,8]
def strangeGrid(r, c):
    #
    # Write your code here.
    add = 0
    if((r-1)%2==1):
        r=r-1
        add = 1
    num_l = even[c-1]+add
    num_h = (r-1)//2

    return num_h*10+num_l

    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
