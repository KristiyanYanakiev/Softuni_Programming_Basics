budget = float(input())
season = input()

total = 0
type = ""
destination = ""

if season == "summer":
    type = "Camp"
elif season == "winter" or destination == "Europe":
    type = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        total = budget * 0.30
    else:
        total = budget * 0.70

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        total = budget * 0.40
    else:
        total = budget * 0.80
else:
    destination = "Europe"
    total = budget * 0.90
    type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type} - {total:.2f}")

