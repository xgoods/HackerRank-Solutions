
user = input('enter a number')

result=[]
for num in range(1,int(user)+1):

    if int(num) % 3 == 0:
        result.append('fizz')

    elif int(num) % 5 == 0:
        result.append('buzz')

    elif int(num) % 3 and int(num) % 5 == 0:
        result.append('fizzbuzz')
    else:
        result.append(num)
    print(num)

print(result)

