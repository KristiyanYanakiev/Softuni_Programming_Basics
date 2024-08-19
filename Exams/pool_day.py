from math import ceil

number_people = int(input())
entrance_fee = float(input())
sun_lounger_price = float(input())
umbrella_price = float(input())

sun_lounger_expenses = (ceil(number_people * 0.75)) * sun_lounger_price
umbrella_expenses = (ceil(number_people * 0.50)) * umbrella_price

total = number_people * entrance_fee + sun_lounger_expenses + umbrella_expenses

print(f"{total:.2f} lv.")


