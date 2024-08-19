import math
from math import sqrt
upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())

valid_data = False
is_prime = False

for a in range(1, upper_limit_first_number + 1):
    for b in range(1, upper_limit_second_number + 1):
        for c in range(1, upper_limit_third_number + 1):

            if a % 2 == 0 and c % 2 == 0 and str(b) in "2357":
                print(f"{a} {b} {c}")


