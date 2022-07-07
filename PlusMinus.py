import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive=0
    negative=0
    zero=0
    total=len(arr)
    
    for num in arr:
        if num > 0:
            positive+=1
        elif num < 0:
            negative+=1
        else:
            zero+=1  
    
    print(round(positive/total,6))
    print(round(negative/total,6))
    print(round(zero/total,6))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
