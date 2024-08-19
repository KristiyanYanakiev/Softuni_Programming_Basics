time = int(input())
day = input()

if 10 <= time <= 18 and (day == "Monday"
                         or day == "Tuesday" or day == "Wednesday"
                         or day == "Thursday" or day == "Friday"
                         or day == "Saturday"):
    print("open")
elif time < 0:
    print("Error")
else:
    print("closed")






