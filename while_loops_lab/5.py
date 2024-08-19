total = 0

while True:
    increase = input()
    if increase != "NoMoreMoney":
        total += float(increase)
        if float(increase) < 0:
            print("Invalid operation")
            break
        print(f"Increase: {float(increase):.2f}")

    else:
        print(f"Total: {total:.2f}")
        break



