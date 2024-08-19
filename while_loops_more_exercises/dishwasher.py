number_bottles_detergent = int(input())

total_ml_detergent = number_bottles_detergent * 750
total_ml_used = 0
counter = 0

dishes_counter = 0
pots_counter = 0

ML_PER_DISH = 5
ML_PER_POT = 15


while total_ml_used < total_ml_detergent:
    counter += 1
    number_of_new = input()
    if number_of_new != "End":
        number_of_new = int(number_of_new)
        if counter % 3 == 0:
            total_ml_used += number_of_new * ML_PER_POT
            pots_counter += number_of_new
        else:
            total_ml_used += number_of_new * ML_PER_DISH
            dishes_counter += number_of_new

    if number_of_new == "End" or total_ml_used > total_ml_detergent:
        if total_ml_used <= total_ml_detergent:
            print("Detergent was enough!")
            print(f"{dishes_counter} dishes and {pots_counter} pots were washed.")
            print(f"Leftover detergent {total_ml_detergent - total_ml_used} ml.")
            break
        else:
            print(f"Not enough detergent, {total_ml_used - total_ml_detergent} ml. more necessary!")
            break
