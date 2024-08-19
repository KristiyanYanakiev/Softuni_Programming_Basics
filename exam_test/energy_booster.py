fruit = input()
size = input()
amount_of_ordered_sets = int(input())

price_per_set = 0

if fruit == "Watermelon":
    if size == "small":
        price_per_set = 56 * 2
    else:
        price_per_set = 28.70 * 5

elif fruit == "Mango":
    if size == "small":
        price_per_set = 36.66 * 2
    else:
        price_per_set = 19.60 * 5
elif fruit == "Pineapple":
    if size == "small":
        price_per_set = 42.10 * 2
    else:
        price_per_set = 24.80 * 5
else:
    if size == "small":
        price_per_set = 20 * 2
    else:
        price_per_set = 15.20 * 5

total = amount_of_ordered_sets * price_per_set

if 400 <= total <= 1000:
    total *= 0.85
elif 1000 < total:
    total *= 0.50

print(f"{total:.2f} lv.")
