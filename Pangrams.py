#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    arr=[]
    d={}
    newS=s.lower()
    let='abcdefghijklmnopqrstuvwxyz'
    count=0
    for i in range (26):
        arr.append(0)
    
    for letter in newS:
        if letter.isalpha and letter not in d:
            d[letter]=1
        elif letter.isalpha and letter in d:
            d[letter]+=1
        else:
            continue
    
    print(d)  
    print(len(arr))
    
    for letter in let:
        if letter not in d.keys():
            print(letter)
            count+=1
            
       
    print(count)
    if count!=0:
        return 'not pangram'
    else:
        return 'pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
