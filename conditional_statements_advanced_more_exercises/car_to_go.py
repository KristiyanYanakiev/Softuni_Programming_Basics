budget = float(input())
season = input()

type_of_car = ""
class_of_car = ""
price_of_car = 0

if budget <= 100:
    class_of_car = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_of_car = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        price_of_car = budget * 0.65

elif 100 < budget <= 500:
    class_of_car = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_of_car = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        price_of_car = budget * 0.80

elif budget > 500:
    class_of_car = "Luxury class"
    type_of_car = "Jeep"
    price_of_car = budget * 0.90

print(class_of_car)
print(f"{type_of_car} - {price_of_car:.2f}")




