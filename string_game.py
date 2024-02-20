
string = input("enter a string: ")
k = input("how many letters do you want to remove? ")

new_k=int(k)
new_string = string[:-new_k]
count={}
print(new_string)
answer = 0
for letter in new_string:
    if letter not in count:
        count[letter] = 0
    count[letter]+=1


for num in count.values():
    answer = ((num**2)+answer)


print(count)
print(answer)
