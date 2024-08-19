percent_of_fat = int(input()) / 100
percent_of_protein = int(input()) / 100
percent_of_carb = int(input()) / 100

total_calories = int(input())

percent_of_water_in_food = int(input()) / 100

grams_from_fat = total_calories * percent_of_fat / 9
grams_from_protein = total_calories * percent_of_protein / 4
grams_from_carb = total_calories * percent_of_carb / 4

total_grams_food = grams_from_protein + grams_from_fat + grams_from_carb

calories_per_gram = total_calories / total_grams_food

final_caloris_per_gram = (1 - percent_of_water_in_food) * calories_per_gram

print(f"{final_caloris_per_gram:.4f}")
