season = input()
group = input()
number_students = int(input())
number_nights = int(input())

sport = ""
price_per_night = 0

if season == "Winter":
    if group == "boys" or group == "girls":
        price_per_night = 9.60
    else:
        price_per_night = 10
        sport = "Ski"
elif season == "Spring":
    if group == "boys" or group == "girls":
        price_per_night = 7.20
    else:
        price_per_night = 9.50
        sport = "Cycling"
else:
    if group == "boys" or group == "girls":
        price_per_night = 15
    else:
        price_per_night = 20
        sport = "Swimming"

total_price = number_nights * price_per_night * number_students

if number_students >= 50:
    total_price *= 0.50
elif 20 <= number_students < 50:
    total_price *= 0.85
elif 10 <= number_students < 20:
    total_price *= 0.95

if season == "Winter":
    if group == "girls":
        sport = "Gymnastics"
    elif group == "boys":
        sport = "Judo"

elif season == "Spring":
    if group == "girls":
        sport = "Athletics"
    elif group == "boys":
        sport = "Tennis"
else:
    if group == "girls":
        sport = "Volleyball"
    elif group == "boys":
        sport = "Football"

print(f"{sport} {total_price:.2f} lv.")
