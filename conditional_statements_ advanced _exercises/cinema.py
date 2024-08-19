movie_type = input()
rows_count = int(input())
cols_count = int(input())

PREMIERE_PRICE = 12
NORMAL_PRICE = 7.50
DISCOUNT = 5

cinema_capacity = rows_count * cols_count
total_price = 0

if movie_type == "Premiere":
    total_price = cinema_capacity * PREMIERE_PRICE
elif movie_type == "Normal":
    total_price = cinema_capacity * NORMAL_PRICE
else:
    total_price = cinema_capacity * DISCOUNT

print(f"{total_price:.2f} leva")
