# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

thisTuple=[]
years_dict = dict()
i=0
j=0
#done
def splitVariable(finalSTR):
    res=""
    for i in finalSTR:
        if(i.isupper()):
            res+="*"+i
        else:
            res+=i
        
    x=res.split("*")
    
    for word in x:
        print(word.lower()+' ',end='')
    print()
def combineMethod(finalSTR2):
    i=0
    joiners=0
    spliters=finalSTR2.split(' ')
    joiners=""
    for var in spliters:
        if i == 1:
            joiners+=(var.capitalize())
        else:
            joiners+=(var)
            i+=1
    print(joiners+'()')
    
def combineClass(finalSTR3):
    i=0
    joiners=0
    spliters=finalSTR3.split(' ')
    joiners=""
    for var in spliters:
        
        i+=1
        joiners+=(var.capitalize())
    
    print(joiners)

def splitClass(finalSTR4):
    res=""
    
    for i in finalSTR4:
        
        if(i.isupper()):
            res+="*"+i
        else:
            res+=i        
    
      
    x=res.split("*")
    x.remove('')
    

    for word in x:
        print(word.lower()+' ',end='')
    print()
    
def splitMethod(finalSTR5):
    res=""
    
    for i in finalSTR5:
        
        if(i.isupper()):
            res+="*"+i
        else:
            res+=i        
    
      
    x=res.split("*")
    #x.remove('')
    

    for word in x:
        if '()' in word:
            print(word[:-2].lower()+' ',end='')
        else:
            print(word.lower()+' ',end='')
    print()
    
def combineVariable(finalSTR6):
    i=0
    joiners=0
    spliters=finalSTR6.split(' ')
    joiners=""
    for var in spliters:
        if i==0:
            joiners+=var
        else:
            joiners+=(var.capitalize())
        
        i+=1
        
    print(joiners)


data=sys.stdin.read().splitlines()

for i in data:
    thisTuple.append(i.split(";"))
        



for tup in thisTuple:
    if tup[0] == 'S' and tup[1] == 'V':
        splitVariable(tup[2])
    if tup[0] == 'C' and tup[1] == 'M':
        combineMethod(tup[2])
    if tup[0] == 'C' and tup[1] == 'C':
        combineClass(tup[2])
    if tup[0] == 'S' and tup[1] == 'C':
        splitClass(tup[2])
    if tup[0] == 'S' and tup[1] == 'M':
        splitMethod(tup[2])
    if tup[0] == 'C' and tup[1] == 'V':
        combineVariable(tup[2])

    
