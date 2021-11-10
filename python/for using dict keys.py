n=int(input("enter a number:"))
d=2
while n>1:
    if n%d==0:
        print(d)
        n=n/d
        continue
    else:
        d=d+1
