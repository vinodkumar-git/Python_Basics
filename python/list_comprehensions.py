l1 = [1,2,3,4,5]
l2 = [2,4,6,8]

print(l1+l2)

l1.append(l2)  #list of list
print(l1)


#adding elemnts of 2 list and out the sum list

l1 = [1,2,3,4,5]
l2 = [2,4,6,8]
x = [i+j for i, j in zip(l1,l2)]
print(x)


x = [i for i in range(1,11)]
print(x)
