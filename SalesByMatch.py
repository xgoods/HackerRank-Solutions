#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    dictionary={}
    count=0
    
    for num in ar:
        if num not in dictionary:
            dictionary[num]=0
        dictionary[num]+=1
    
    
    for num in dictionary.values():
        temp = math.floor(num/2)
        count+=temp
        
            
    
    print(dictionary)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
