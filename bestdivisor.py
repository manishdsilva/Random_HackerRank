#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    best = 1
    for i in range(2,n+1):
        if(n%i == 0):
            if(sum(map(int, str(i)))>sum(map(int, str(best)))):
                best = i
    print(best)
