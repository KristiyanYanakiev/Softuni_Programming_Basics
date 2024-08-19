total = 0
half = 0
n = int(input())
number = 0


for i in range(n):
    number = int(input())
    total += number

for i in range(n // 2):
    half += number

print(half)