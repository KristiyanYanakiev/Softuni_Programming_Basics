fruit = input()
day = input()
quantity = float(input())
price = 0
correct_data = True

if fruit == "banana":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.50
    elif day == "Saturday" or day == "Sunday":
        price = 2.70
    else:
        correct_data = False

elif fruit == "apple":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.20
    elif day == "Saturday" or day == "Sunday":
        price = 1.25
    else:
        correct_data = False
elif fruit == "orange":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 0.85
    elif day == "Saturday" or day == "Sunday":
        price = 0.90
    else:
        correct_data = False
elif fruit == "grapefruit":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.45
    elif day == "Saturday" or day == "Sunday":
        price = 1.60
    else:
        correct_data = False
elif fruit == "kiwi":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.70
    elif day == "Saturday" or day == "Sunday":
        price = 3.00
    else:
        correct_data = False
elif fruit == "pineapple":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 5.50
    elif day == "Saturday" or day == "Sunday":
        price = 5.60
    else:
        correct_data = False
elif fruit == "grapes":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 3.85
    elif day == "Saturday" or day == "Sunday":
        price = 4.20
    else:
        correct_data = False
else:
    correct_data = False


total = quantity * price

if correct_data:
    print(f"{total:.2f}")
else:
    print("error")


