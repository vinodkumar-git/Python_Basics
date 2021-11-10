s1 = "vinod"
s2 = "kumar"

#REPLACE A CHARACTER IN A STRING
lis = list(s1)  #convert string to list as string is immutable

l = len(lis)    #len is 5

for i in range(l):  #0 to 4
    if lis[i] == 'v':
        lis[i] = 'V'

#TO PRINT LIST ELEMENTS AS STRING
s = "".join(lis)  
s1 = "-".join(lis)  #use of join
print(s,'\n',s1)

#OR

s = ['v', 'i', 'n']  #another way to print list elements are string using concat
str = ""
for ele in s:
    str = str + ele
print(str)



#CONCAT 2 STRING WITHOUT USING + OPERATOR
x = "Hello"
y = "world"
l1 = list(x)
l2 = list(y)

for i in l2:
    l1.append(i)
print(l1)
#convert list to string
print("".join(l1))

#OR very silly way
print(x+" "+y)

    





