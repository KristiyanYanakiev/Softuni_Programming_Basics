from math import floor

record = float(input())
distance = float(input())
seconds_per_meter = float(input())

resistance = floor(distance / 50) * 30

result = distance * seconds_per_meter + resistance

if result < record:
    print(f"Yes! The new record is {result:.2f} seconds.")
else:
    print(f"No! He was {result - record:.2f} seconds slower.")