city = input()
type = input()
vip_discount = input()
days = int(input())

price_per_day = 0
correct_data = True

if city == "Bansko" or city == "Borovets":
    if type == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.90
    elif type == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day *= 0.95
    else:
        correct_data = False

elif city == "Varna" or city == "Burgas":
    if type == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day *= 0.88
    elif type == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.93
    else:
        correct_data = False
else:
    correct_data = False

if days > 7:
    days = days - 1

total = days * price_per_day


if correct_data and days >= 1:
    print(f"The price is {total:.2f}lv! Have a nice time!")
elif correct_data and days < 1:
    print(f"Days must be positive number!")
else:
    print("Invalid input!")