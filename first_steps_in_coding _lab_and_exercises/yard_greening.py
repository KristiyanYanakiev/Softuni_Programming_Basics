total_square_meters = float(input())
total_price=total_square_meters * 7.61
total_price_with_discount = total_price - total_price * 0.18
discount = total_price * 0.18

print(f'The final price is {total_price_with_discount} lv.')
print (f'The discount is {discount}')


