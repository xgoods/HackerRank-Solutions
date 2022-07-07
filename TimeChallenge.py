#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
#12->0
#1-11am->same
#12pm->same
#1pm-13
#2pm-14
#3pm-15
#4pm-16
#5pm-17
#6pm-18
#7pm-19
#8pm-20
#9pm-21
#10pm-22
#11pm-23
def timeConversion(s):
    # Write your code here
    newTime=s.split(":")
    if(newTime[0]=='12' and 'AM' in newTime[2]):
        newTime[0]='00'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
    
    if(newTime[0]=='01' and 'AM' in newTime[2]):
        newTime[0]='01'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
    
    if(newTime[0]=='02' and 'AM' in newTime[2]):
        newTime[0]='02'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
    
    
    if(newTime[0]=='03' and 'AM' in newTime[2]):
        newTime[0]='03'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='04' and 'AM' in newTime[2]):
        newTime[0]='04'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='05' and 'AM' in newTime[2]):
        newTime[0]='05'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='06' and 'AM' in newTime[2]):
        newTime[0]='06'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='07' and 'AM' in newTime[2]):
        newTime[0]='07'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='08' and 'AM' in newTime[2]):
        newTime[0]='08'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='09' and 'AM' in newTime[2]):
        newTime[0]='09'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='10' and 'AM' in newTime[2]):
        newTime[0]='10'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='11' and 'AM' in newTime[2]):
        newTime[0]='11'
        newTime[2]=newTime[2].replace('AM','')
        finalTime=':'.join(newTime)
    
    #PM PM PM PM PM PM
    
    if(newTime[0]=='12' and 'PM' in newTime[2]):
        newTime[0]='12'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
    
    if(newTime[0]=='01' and 'PM' in newTime[2]):
        newTime[0]='13'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='02' and 'PM' in newTime[2]):
        newTime[0]='14'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='03' and 'PM' in newTime[2]):
        newTime[0]='15'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='04' and 'PM' in newTime[2]):
        newTime[0]='16'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
    
    if(newTime[0]=='05' and 'PM' in newTime[2]):
        newTime[0]='17'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='06' and 'PM' in newTime[2]):
        newTime[0]='18'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='07' and 'PM' in newTime[2]):
        newTime[0]='19'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)

    if(newTime[0]=='08' and 'PM' in newTime[2]):
        newTime[0]='20'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='09' and 'PM' in newTime[2]):
        newTime[0]='21'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
    
    if(newTime[0]=='10' and 'PM' in newTime[2]):
        newTime[0]='22'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
        
    if(newTime[0]=='11' and 'PM' in newTime[2]):
        newTime[0]='23'
        newTime[2]=newTime[2].replace('PM','')
        finalTime=':'.join(newTime)
    
    return str(finalTime)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()