drink_type = input()
sugar = input()
drink_count = int(input())

espresso_price = 0
capuccino_price = 0
tea_price = 0
total = 0

if drink_type == "Espresso":
    total = drink_count * espresso_price
elif drink_type == "Cappuccino":
    total = drink_count * capuccino_price
else:
    total = drink_count * tea_price

if drink_type == "Espresso":
    if sugar == "Without":
        espresso_price = 0.90
    elif sugar == "Normal":
        espresso_price = 1
    else:
        espresso_price = 1.20
elif drink_type == "Cappuccino":
    if sugar == "Without":
        capuccino_price = 1.00
    elif sugar == "Normal":
        capuccino_price = 1.20
    else:
        capuccino_price = 1.60
else:
    if sugar == "Without":
        tea_price = 0.50
    elif sugar == "Normal":
        tea_price = 0.60
    else:
        tea_price = 0.70

if sugar == "Without":
    espresso_price *= 0.65
    capuccino_price *= 0.65
    tea_price *= 0.65

if drink_type == "Espresso" and drink_count >= 5:
    espresso_price *= 0.75

if drink_type == "Espresso":
    total = drink_count * espresso_price
elif drink_type == "Cappuccino":
    total = drink_count * capuccino_price
else:
    total = drink_count * tea_price

if total > 15:
    total *= 0.80

print(f"You bought {drink_count} cups of {drink_type} for {total:.2f} lv.")