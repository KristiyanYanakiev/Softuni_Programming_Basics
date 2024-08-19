from math import floor
from math import ceil

a = int(input())
grapes_per_one_square_km = float(input())
needed_liters_of_wine = int(input())
number_of_workers = int(input())

a_for_wine = a * 0.40
produced_grapes_for_wine = grapes_per_one_square_km * a_for_wine
produced_liters_of_wine = produced_grapes_for_wine / 2.5

left_wine = produced_liters_of_wine - needed_liters_of_wine
left_wine_per_worker = left_wine / number_of_workers

if produced_liters_of_wine < needed_liters_of_wine:
    print(f"It will be a tough winter! More {floor(needed_liters_of_wine - produced_liters_of_wine)} liters wine needed.")
elif produced_liters_of_wine >= needed_liters_of_wine:
    print(f"Good harvest this year! Total wine: {floor(produced_liters_of_wine)} liters.")
    print(f"{ceil(left_wine)} liters left -> {ceil(left_wine_per_worker)} liters per person.")
