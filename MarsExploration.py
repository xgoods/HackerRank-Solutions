#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    sos='SOS'
    newSOS=''
    count=0
    counter=0
    
    j=0
    arr=[]
    
    for letter in s:
        count+=1
        newSOS+=letter
        if count==3:
            newSOS+='*'
            count=0
            
    x=newSOS.split("*")        
    
    for item in x:
        if item == '':
            x.remove(item)
    
    
    for i in range(len(x)):
        if x[i][0] != 'S':
            counter+=1
        if x[i][1] != 'O':
            counter+=1
        if x[i][2] != 'S':
            counter+=1   
    
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
