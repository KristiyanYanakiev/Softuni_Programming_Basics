vacation_price = float(input())
puzles_count = int(input())
speaking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

PUZLE_PRICE = 2.60
SPEAKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

total_count = puzles_count + speaking_dolls_count + teddy_bears_count + minions_count + trucks_count
total_price = puzles_count * PUZLE_PRICE \
              + speaking_dolls_count * SPEAKING_DOLL_PRICE\
              + teddy_bears_count * TEDDY_BEAR_PRICE \
              + minions_count * MINION_PRICE \
              + trucks_count * TRUCK_PRICE

if total_count >= 50:
    total_price = total_price - (total_price * 0.25)

rent = total_price * 0.10

total_price = total_price - rent

if total_price >= vacation_price:
    print(f"Yes! {total_price - vacation_price:.2f} lv left.")
elif total_price < vacation_price:
    print(f"Not enough money! {vacation_price - total_price:.2f} lv needed.")

