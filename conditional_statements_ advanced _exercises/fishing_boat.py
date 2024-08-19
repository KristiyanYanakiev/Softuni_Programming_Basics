budget = int(input())
season = input()
fishers_count = int(input())

total = 0

if season == "Spring":
    total = 3000
elif season == "Summer" or season == "Autumn":
    total = 4200
else:
    total = 2600

if fishers_count <= 6:
    total *= 0.90
elif 7 <= fishers_count <= 11:
    total *= 0.85
elif fishers_count >= 12:
    total *= 0.75

if fishers_count % 2 == 0 and season != "Autumn":
    total *= 0.95


if total <= budget:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - total):.2f} leva.")






