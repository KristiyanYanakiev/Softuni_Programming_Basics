month = input()
nights_count = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights_count <= 14:
        studio *= 0.95
    elif nights_count > 14:
        studio *= 0.70


elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights_count > 14:
        studio *= 0.80

elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if nights_count > 14:
    apartment *= 0.90

total_apartment = nights_count * apartment
total_studio = nights_count * studio

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
