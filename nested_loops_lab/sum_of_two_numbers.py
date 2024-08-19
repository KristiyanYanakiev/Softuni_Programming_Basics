a = int(input())
b = int(input())

magic_number = int(input())

combination_counter = 0

for first_number in range(a, b + 1):
    for second_number in range(a, b + 1):
        combination_counter += 1

        if first_number + second_number == magic_number:
            print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
            exit()
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")




