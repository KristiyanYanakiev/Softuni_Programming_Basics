n = int(input())

number = 0
total_left = 0
total_right = 0

for i in range(n):
    number = int(input())
    total_left += number

for i in range(n):
    number = int(input())
    total_right += number

if total_left == total_right:
    print(f"Yes, sum = {total_left}")
else:
    print(f"No, diff = {abs(total_left - total_right)}")



