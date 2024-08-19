n = int(input())

max_number = float("-inf")
total = 0

for _ in range(n):
    number = int(input())
    total += number
    if number > max_number:
        max_number = number

if max_number == total - max_number:
    print(f"Yes \nSum = {max_number}")
else:
    print(f"No \nDiff = {abs((total - max_number) - max_number)}")


