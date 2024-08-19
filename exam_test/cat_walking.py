minutes_walk_per_day = int(input())
number_of_walks_per_day = int(input())
calories_eaten_oer_day = int(input())

calories_expended = number_of_walks_per_day * minutes_walk_per_day * 5

if calories_expended >= calories_eaten_oer_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_expended}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_expended}.")
