def reverse(s): 
  str = "" 
  for i in s:
    print(i)
    str = i + str
  return str

s = "vinod"
  
print ("The original string  is : ",s) 
  
print ("The reversed string(using loops) is :", reverse(s))

#OR

print("another type of reversing is: ", s[::-1])
 #OR
print("using builtin function", reverse(s))
