string=input("ENTER THE STRING:")

new_string=""

liststring=list(string)
print(liststring)

len_liststring=len(liststring)
print(len_liststring)

for i in range(len_liststring-1):  #for iteration or cycle
    #print("step:",i)
    for j in range(len_liststring-i-1): #compare 2 chars j and j+1 and swap in each loop
        #print("j:{}\n".format(j))
        if liststring[j]>liststring[j+1]:
            liststring[j],liststring[j+1]=liststring[j+1],liststring[j]
            #print(liststring)

for m in liststring:    #to convert the list to string
    new_string+=m
print("-----------------")
print(new_string,"IS THE STORTED STRING")
    
