#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    pathArr=[]
    i=0
    vals=0
    count=0
    for direction in path:
        pathArr.append(direction)
        
    for direction in pathArr:
        if count == 0 and direction == 'D':
            vals+=1
    
        if direction == 'D':
            count-=1
        if direction =='U':
            count+=1
        
            
    print(vals)
    return vals
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
