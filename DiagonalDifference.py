#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    i=0
    j=0
    l=(n-1)    
    
    lDiag=[]
    rDiag=[]
    for k in range(n):
        print('here')
        
        lDiag.append(arr[k][j])
        i+=1
        j+=1
        
    for k in range(n):
        
        rDiag.append(arr[k][l])
        l-=1
    
    total=sum(lDiag)-sum(rDiag)
    return abs(total)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
