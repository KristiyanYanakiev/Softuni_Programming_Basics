best_player_name = ""
best_player_score = 0


while True:
    data = input()

    if data == "END":
        break

    player_name = data
    number_of_goals = int(input())

    if number_of_goals > best_player_score:
        best_player_score = number_of_goals
        best_player_name = player_name

    if number_of_goals >= 10:
        break

print(f"{best_player_name} is the best player!")

if best_player_score >= 3:
    print(f"He has scored {best_player_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_score} goals.")


