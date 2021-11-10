def checkmoney(sis):
    if sis<7000 :
        print("ahem, can you rethink this number please?")
    elif sis>10000:
        print("Wow sis! You are a queen")
    elif sis in range(7000,10001):  #instead of elif sis>7000 and sis<10000:
        print("cool, thanks sis! {} rupees will certainly help".format(sis))

    return

sis=int(input("enter the amout sis would like to offer to pi:"))
checkmoney(sis)
