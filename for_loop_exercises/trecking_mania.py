number_of_groups = int(input())

musala_people = 0
montblan_people = 0
kilimandjaro_people = 0
k2_people = 0
everest_people = 0
total_number_of_people = 0

for _ in range(number_of_groups):
    number_of_people_in_a_group = int(input())
    total_number_of_people += number_of_people_in_a_group
    if number_of_people_in_a_group <= 5:
        musala_people += number_of_people_in_a_group
    elif 6 <= number_of_people_in_a_group <= 12:
        montblan_people += number_of_people_in_a_group
    elif 13 <= number_of_people_in_a_group <= 25:
        kilimandjaro_people += number_of_people_in_a_group
    elif 26 <= number_of_people_in_a_group <= 40:
        k2_people += number_of_people_in_a_group
    elif 41 <= number_of_people_in_a_group:
        everest_people += number_of_people_in_a_group

print(f"{musala_people / total_number_of_people * 100:.2f}%")
print(f"{montblan_people / total_number_of_people * 100:.2f}%")
print(f"{kilimandjaro_people / total_number_of_people * 100:.2f}%")
print(f"{k2_people / total_number_of_people * 100:.2f}%")
print(f"{everest_people / total_number_of_people * 100:.2f}%")