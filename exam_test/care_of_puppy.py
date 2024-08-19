bought_food = int(input()) * 1000

total_eaten_food = 0

while True:
    eaten_food = input()
    if eaten_food != "Adopted":
        eaten_food = int(eaten_food)
        total_eaten_food += eaten_food
    else:
        if total_eaten_food <= bought_food:
            print(f"Food is enough! Leftovers: {bought_food - total_eaten_food} grams.")
            break
        else:
            print(f"Food is not enough. You need {total_eaten_food - bought_food} grams more.")
            break


