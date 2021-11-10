arr = [1,5,2,8,3,8,2,4,2,9]
print(max(set(arr), key=arr.count))


#OR

arr = [1,2,3,3,3,3,2,3,2,2,4]

r = max(set(arr), key=arr.count)
print(r)




