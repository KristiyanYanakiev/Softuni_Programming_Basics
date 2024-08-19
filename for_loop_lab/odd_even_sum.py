n = int(input())
even_total = 0
odd_total = 0

for i in range(n):
    current_number = int(input())
    if i % 2 == 0:
        even_total += current_number
    else:
        odd_total += current_number

if even_total == odd_total:
    print("Yes")
    print(f"Sum = {even_total}")
else:
    print("No")
    print(f"Diff = {abs(even_total - odd_total)}")