city = input()
sales = float(input())

commission = 0
correct_date = True


if 0 <= sales <= 500:
    if city == "Sofia":
        commission = sales * 0.05
    elif city == "Varna":
        commission = sales * 0.045
    elif city == "Plovdiv":
        commission = sales * 0.055
    else:
        correct_date = False

elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = sales * 0.07
    elif city == "Varna":
        commission = sales * 0.075
    elif city == "Plovdiv":
        commission = sales * 0.08
    else:
        correct_date = False
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = sales * 0.08
    elif city == "Varna":
        commission = sales * 0.10
    elif city == "Plovdiv":
        commission = sales * 0.12
    else:
        correct_date = False
elif sales > 10000:
    if city == "Sofia":
        commission = sales * 0.12
    elif city == "Varna":
        commission = sales * 0.13
    elif city == "Plovdiv":
        commission = sales * 0.145
    else:
        correct_date = False
else:
    correct_date = False

if correct_date:
    print(f"{commission:.2f}")
else:
    print("error")
