number_of_days = int(input())
total_amount_of_food = float(input())

amount_of_biscuits = 0
total_eaten_amount = 0
total_eaten_from_dog = 0
total_eaten_from_cat = 0

for i in range(1, number_of_days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())
    if i % 3 == 0:
        amount_of_biscuits += 0.10 * (food_eaten_by_dog + food_eaten_by_cat)

    total_eaten_from_dog += food_eaten_by_dog
    total_eaten_from_cat += food_eaten_by_cat
    total_eaten_amount = total_eaten_from_dog + total_eaten_from_cat


print(f"Total eaten biscuits: {round(amount_of_biscuits)}gr.")
print(f"{total_eaten_amount / total_amount_of_food * 100:.2f}% of the food has been eaten.")
print(f"{total_eaten_from_dog / total_eaten_amount * 100:.2f}% eaten from the dog.")
print(f"{total_eaten_from_cat / total_eaten_amount * 100:.2f}% eaten from the cat.")


