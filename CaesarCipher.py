#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabetU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift=[]
    check = False
    
    while k > 26:
        k-=26
    
    for letter in s:
        check = False
        if letter.isupper():
            temp = alphabetU.find(letter)
            check = True
        else:
            temp = alphabet.find(letter)
            check = False
    
        tempNum = int(temp) + k
        if tempNum >= 26 and check is False:
            tempNum = tempNum - 26
            shift.append(alphabet[tempNum])
        elif letter in string.punctuation and check is False:
            
            shift.append(letter)
        elif letter.isnumeric() and check is False:
            shift.append(letter)
        elif check is False:
            
            shift.append(alphabet[tempNum])
            
        if tempNum >= 26 and check is True:
            tempNum = tempNum - 26
            shift.append(alphabetU[tempNum])
        elif letter in string.punctuation and check is True:
            shift.append(letter)
        elif letter.isnumeric() and check is True:
            shift.append(letter)
        elif check is True:
            shift.append(alphabetU[tempNum])
        
    cipher = ''.join(shift)
    return cipher
           
            
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
