type_of_flowers = input()
flowers_count = int(input())
budget = int(input())

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50
total = 0

if type_of_flowers == "Roses":
    total = flowers_count * ROSES_PRICE
    if flowers_count > 80:
        total *= 0.90
elif type_of_flowers == "Dahlias":
    total = flowers_count * DAHLIAS_PRICE
    if flowers_count > 90:
        total *= 0.85
elif type_of_flowers == "Tulips":
    total = flowers_count * TULIPS_PRICE
    if flowers_count > 80:
        total *= 0.85
elif type_of_flowers == "Narcissus":
    total = flowers_count * NARCISSUS_PRICE
    if flowers_count < 120:
        total = total + total * 0.15
elif type_of_flowers == "Gladiolus":
    total = flowers_count * GLADIOLUS_PRICE
    if flowers_count < 80:
        total = total + total * 0.20

if total <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {budget - total:.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")

