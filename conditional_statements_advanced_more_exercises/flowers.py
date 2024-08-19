number_chrysanthemums = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holiday_or_not = input()

chrysanthemum_price = 0
roses_price = 0
tulip_price = 0
total = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2.00
    roses_price = 4.10
    tulip_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulip_price = 4.15

total = number_chrysanthemums * chrysanthemum_price + number_roses * roses_price + number_tulips * tulip_price

if holiday_or_not == "Y":
    total = total + total * 0.15

if number_tulips > 7 and season == "Spring":
    total = total - total * 0.05

if number_roses >= 10 and season == "Winter":
    total = total - total * 0.10

if number_roses + number_tulips + number_chrysanthemums > 20:
    total = total - total * 0.20

final_total = total + 2

print(f"{final_total:.2f}")


