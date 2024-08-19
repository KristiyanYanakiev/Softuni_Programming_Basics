days = float(input())
type_of_room = input()
score = input()

ROOM_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

nights = days - 1
total = 0

if days < 10:
    APARTMENT *= 0.70
    PRESIDENT_APARTMENT *= 0.90
elif 10 <= days <= 15:
    APARTMENT *= 0.65
    PRESIDENT_APARTMENT *= 0.85
elif days > 15:
    APARTMENT *= 0.50
    PRESIDENT_APARTMENT *= 0.80

if type_of_room == "apartment":
    total = nights * APARTMENT
elif type_of_room == "president apartment":
    total = nights * PRESIDENT_APARTMENT
else:
    total = nights * ROOM_ONE_PERSON

if score == "positive":
    total = total + total * 0.25
else:
    total *= 0.90

print(f"{total:.2f}")


