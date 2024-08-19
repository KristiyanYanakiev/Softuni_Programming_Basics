name_of_actor = input()
points_from_academy = float(input())
number_of_jury_members = int(input())

total_from_all_judges = 0
total_points = 0


for _ in range(number_of_jury_members):
    name_of_judge = input()
    points_from_judge = float(input())
    final_points_from_judge = ((len(name_of_judge)) * points_from_judge) / 2
    total_from_all_judges += final_points_from_judge

    total_points = points_from_academy + total_from_all_judges

    if total_points > 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {name_of_actor} you need {1250.5 - total_points:.1f} more!")

