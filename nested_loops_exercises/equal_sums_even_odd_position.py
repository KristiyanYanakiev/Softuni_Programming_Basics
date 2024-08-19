number_one, number_two = int(input()), int(input())

for number in range(number_one, number_two + 1):
    sum_even = 0
    sum_odd = 0

    for index, digit in enumerate(str(number)):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(number, end=" ")

