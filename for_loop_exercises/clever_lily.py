age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_count = 0
money_given = 0
total_money_given = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toy_count += 1
    elif i % 2 == 0:
       money_given += 10
       total_money_given += money_given - 1

total = total_money_given + toy_price * toy_count

if total >= washing_machine_price:
    print(f"Yes! {total - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total:.2f}")

