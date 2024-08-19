import math

number_of_tournaments = int(input())
starting_points = int(input())

won_points = 0
average_points = 0
number_of_won_tournaments = 0

for _ in range(number_of_tournaments):
    result = input()
    if result == "W":
        won_points += 2000
        number_of_won_tournaments += 1
    elif result == "F":
        won_points += 1200
    elif result == "SF":
        won_points += 720

final_points = starting_points + won_points
average_points = won_points / number_of_tournaments
percentage_of_won_tournaments = number_of_won_tournaments / number_of_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_of_won_tournaments:.2f}%")