day=0
squats=0
total=0

print("Enter number of squates done on each day...")

while day<=6:
    day=day+1
    squats=int(input("number of squats done on day {}:".format(day)))
    total=total+squats

avg=total/day
print("in last {} days, you did an average of {} squats!".format(day,avg))
