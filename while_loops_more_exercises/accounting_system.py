required_amount = int(input())
count = 0
card_payments = 0
total_amount_cards = 0
cash_payments = 0
total_amount_cash = 0

while True:
    count += 1
    product_price = input()
    if product_price != "End":
        product_price = int(product_price)
        if count % 2 == 0:
            if product_price >= 10:
                print("Product sold!")
                card_payments += 1
                total_amount_cards += product_price
            else:
                print("Error in transaction!")

        else:
            if product_price <= 100:
                print("Product sold!")
                cash_payments += 1
                total_amount_cash += product_price

            else:
                print("Error in transaction!")

    elif product_price == "End":
        print("Failed to collect required money for charity.")
        break

    if total_amount_cash + total_amount_cards >= required_amount:
        print(f"Average CS: {total_amount_cash / cash_payments:.2f}")
        print(f"Average CC: {total_amount_cards / card_payments:.2f}")
        break




