#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    dictionary={}
    count=[]
    maximum=0
    
    for num in arr:
        if num not in dictionary:
            dictionary[num]=0
        dictionary[num]+=1
    
    
    temp=max(dictionary.values())
    
    for key,value in dictionary.items():
        if temp==value:
            count.append(key)
            
    finCount=min(count)
    print(dictionary)
    return finCount
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
