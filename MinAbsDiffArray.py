#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    temp = 0
    minArr=[]
    for i in (list(combinations(arr,2))):
        print(i)
        temp = abs(i[0]-(i[1]))
        minArr.append(temp)
    print(minArr)
    minimum=min(minArr)
    
    return minimum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()