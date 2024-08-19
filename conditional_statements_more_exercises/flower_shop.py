from math import floor
from math import ceil



number_of_magnolias = int(input())
number_of_zumbuls = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
present_price = float(input())


total = (number_of_magnolias * 3.25 + number_of_zumbuls * 4 + number_of_roses * 3.50 + number_of_cactus * 8)

final = total - (total * 0.05)

if final >= present_price:
    print(f"She is left with {floor(final - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - final)} leva.")