number_of_pens = int(input())
number_of_markers = int(input())
litters_of_cleaning_material = int(input())
discount = int(input()) / 100

total_price = number_of_pens * 5.80 + number_of_markers * 7.20 + litters_of_cleaning_material * 1.20
total_price_with_discount = total_price - total_price * discount

print(total_price_with_discount)




