type_fuel = input()
liters = float(input())
discount_card = input()

total = 0

if type_fuel == "Gasoline":
    total = liters * 2.22
    if discount_card == "Yes":
        total = liters * (2.22 - 0.18)

elif type_fuel == "Diesel":
    total = liters * 2.33
    if discount_card == "Yes":
        total = liters * (2.33 - 0.12)
else:
    total = liters * 0.93
    if discount_card == "Yes":
        total = liters * (0.93 - 0.08)

if 20 <= liters <= 25:
    total *= 0.92
elif liters > 25:
    total *= 0.90

print(f"{total:.2f} lv.")