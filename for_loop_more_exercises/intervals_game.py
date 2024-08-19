number_of_moves = int(input())

result = 0
from_0_to_10 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for _ in range(number_of_moves):
    number = int(input())
    if 0 <= number <= 9:
        result += number * 0.20
        from_0_to_10 += 1
    elif 10 <= number <= 19:
        result += number * 0.30
        from_10_to_19 += 1
    elif 20 <= number <= 29:
        result += number * 0.40
        from_20_to_29 += 1
    elif 30 <= number <= 39:
        result += 50
        from_30_to_39 += 1
    elif 40 <= number <= 50:
        result += 100
        from_40_to_50 += 1
    elif number > 50 or number < 0:
        result /= 2
        invalid_numbers += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {from_0_to_10 / number_of_moves * 100:.2f}%")
print(f"From 10 to 19: {from_10_to_19 / number_of_moves * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / number_of_moves * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / number_of_moves * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / number_of_moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / number_of_moves * 100:.2f}%")
