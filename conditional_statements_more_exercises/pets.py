from math import ceil
from math import floor


number_of_day = int(input())
left_food_in_kgs = int(input())
food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input()) / 1000

total_dog_food_needed = food_per_day_dog * number_of_day
total_cat_food_needed = food_per_day_cat * number_of_day
total_turtle_food_needed = food_per_day_turtle * number_of_day

total_food_needed = total_dog_food_needed + total_cat_food_needed + total_turtle_food_needed

if total_food_needed <= left_food_in_kgs:
    print(f"{floor(left_food_in_kgs - total_food_needed)} kilos of food left.")
else:
    print(f"{ceil(total_food_needed - left_food_in_kgs)} more kilos of food are needed.")
