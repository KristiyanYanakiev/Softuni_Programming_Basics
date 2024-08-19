starting_amount = float(input())
sex = input()
age = int(input())
sport = input()

card_price = 0

if sport == "Gym":
    if sex == "m":
        card_price = 42
    else:
        card_price = 35

elif sport == "Boxing":
    if sex == "m":
        card_price = 41
    else:
        card_price = 37
elif sport == "Yoga":
    if sex == "m":
        card_price = 45
    else:
        card_price = 42
elif sport == "Zumba":
    if sex == "m":
        card_price =34
    else:
        card_price = 31
elif sport == "Dances":
    if sex == "m":
        card_price = 51
    else:
        card_price = 53
else:
    if sex == "m":
        card_price = 39
    else:
        card_price = 37

if age <= 19:
    card_price *= 0.80

if card_price <= starting_amount:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${card_price - starting_amount:.2f} more.")
