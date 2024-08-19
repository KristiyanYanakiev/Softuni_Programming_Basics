import sys

max_dif = - sys.maxsize

n = int(input()) * 2

total = 0
pair_counter = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        total += number
        pair_counter += 1
    if pair_counter % 2 == 0:
        




















