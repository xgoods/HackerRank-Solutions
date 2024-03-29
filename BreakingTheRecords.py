#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#testingtestngs

def breakingRecords(scores):
    # Write your code here
    #testing commits
    minimum=0
    maximum=0
    temp=scores[0]
    for num in scores:
        if num>temp:
            temp=num
            maximum+=1
    temp=scores[0]
    for num in scores:    
        if num < temp:
            temp=num
            minimum+=1
    
    finalScore=(maximum,minimum)
    return finalScore
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()