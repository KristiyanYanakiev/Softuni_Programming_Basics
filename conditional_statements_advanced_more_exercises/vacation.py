budget = float(input())
season = input()

location = ""
place = ""
price = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    place = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} – {place} – {price:.2f}")


