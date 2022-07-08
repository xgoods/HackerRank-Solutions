#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    finArr=[]
    rounders=[100,95,90,85,80,75,70,65,60,55,50,45, 40]
    
    for num in grades:
        if (num+2) in rounders and (num+2) >= 40:
            num=num+2
            finArr.append(num)
        elif (num+1) in rounders and (num+1) >= 40:
            num=num+1
            finArr.append(num)
        else:
            finArr.append(num)
    
    return finArr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
