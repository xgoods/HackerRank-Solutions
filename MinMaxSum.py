#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    temp=0
    temp2=0
    minArr=[]
    maxArr=[]
    sameArr=[]
    i=0
    count = 0
    count2 = 0
    count3 = 0
    
    for num in arr:
        for temp in arr:
            if num > temp:
                maxArr.append(num)
    
    for num in arr:
        for temp in arr:
            if num < temp:
                minArr.append(num)
                
        
    finalMaxArr = set(maxArr)
    finalMinArr = set(minArr)
    
    for num in finalMaxArr:
        count+=num
        
    for num in finalMinArr:
        count2+=num
        
        
    print(int(count2), int(count))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
