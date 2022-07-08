#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    #print(c_int32(n).value)
    test=(bin(n)[2:].zfill(32))
    test2=test.replace('1', '2').replace('0', '1').replace('2', '0')
    return (int(test2,2))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
