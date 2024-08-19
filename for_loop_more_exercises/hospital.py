current_doctors = 7
treated_patients = 0
untreated_patients = 0

period = int(input())

for i in range(1, period +1):
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            current_doctors += 1
    current_patients = int(input())
    if current_patients > current_doctors:
        current_patients -= current_patients - current_doctors
        treated_patients += current_patients
        untreated_patients -= current_patients - current_doctors

print(treated_patients)
print(untreated_patients)






