#DCITIONARY COMPREHENSIONS:

from string import ascii_lowercase
x = {i:j for i,j in enumerate(ascii_lowercase) if i < 6}
#Enumerate () adds a counter to the elements in the list. Takes 2 args(listname, start=0 //default is 0)
#eg: [1: 'a', 2: 'c', 3: 'ad']
print(x)

print("----------------------")

x = {j:i for i,j in enumerate(ascii_lowercase) if i < 6}
print(x)

print("---------------------")

x = {i:i for i in range(1,11)}
print(x)
