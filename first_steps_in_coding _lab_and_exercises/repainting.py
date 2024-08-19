needed_plastic_bags = int(input())
needed_quantity_of_paint = int(input())
needed_quantity_solution = int(input())
hours_workers = int(input())

PLASTIC_BAG = 1.50
PAINT = 14.50
SOLUTION = 5.00
BAG_PRICE = 0.40

total_plastic_bags = needed_plastic_bags * PLASTIC_BAG + 2 * PLASTIC_BAG
quantity_of_pain = needed_quantity_of_paint * PAINT
total_quantity_of_paint = quantity_of_pain + quantity_of_pain * 0.10
total_quantity_solution = needed_quantity_solution * SOLUTION

sum_total = total_plastic_bags + total_quantity_of_paint + total_quantity_solution + 0.40
total_workers_expenses = hours_workers * (sum_total * 0.30)

final_sum_total = sum_total + total_workers_expenses

print({final_sum_total})

