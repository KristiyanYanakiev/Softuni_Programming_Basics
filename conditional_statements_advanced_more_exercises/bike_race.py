number_juniors = int(input())
number_seniors = int(input())
type_trace = input()

junior_fee = 0
senior_fee = 0
final_total = 0

if type_trace == "trail":
    junior_fee = 5.50
    senior_fee = 7
elif type_trace == "cross-country":
    junior_fee = 8
    senior_fee = 9.50
elif type_trace == "downhill":
    junior_fee = 12.25
    senior_fee = 13.75
else:
    junior_fee = 20
    senior_fee = 21.50

total_participation = number_juniors * junior_fee + number_seniors * senior_fee

if type_trace == "cross-country" and number_juniors + number_seniors >= 50:
    total_participation *= 0.75

final_total = total_participation * 0.95

print(f"{final_total:.2f}")
