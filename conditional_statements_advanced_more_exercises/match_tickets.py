budget = float(input())
category = input()
number_of_people = int(input())

ticket_price = 0
travel_expenses = 0
VIP_PRICE = 499.99
NORMAL_PRICE = 249.99

if 1 <= number_of_people <= 4:
    travel_expenses = budget * 0.75
elif 5 <= number_of_people <= 9:
    travel_expenses = budget * 0.60
elif 10 <= number_of_people <= 24:
    travel_expenses = budget * 0.50
elif 25 <= number_of_people <= 49:
    travel_expenses = budget * 0.40
elif number_of_people >= 50:
    travel_expenses = budget * 0.25

if category == "VIP":
    ticket_price = VIP_PRICE
else:
    ticket_price = NORMAL_PRICE

total = number_of_people * ticket_price + travel_expenses

if total <= budget:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")