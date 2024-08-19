CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETERIAN_MENU = 8.15

number_of_chicken_menu = int(input()) * CHICKEN_MENU
number_of_fish_menu = int(input()) * FISH_MENU
number_of_vegeterian_menu = int(input()) * VEGETERIAN_MENU

desert = (number_of_chicken_menu + number_of_fish_menu + number_of_vegeterian_menu) * 0.2
food_delivery = 2.50

final_price = number_of_chicken_menu + number_of_fish_menu + number_of_vegeterian_menu + desert + food_delivery

print(f"{final_price:.02f}")

