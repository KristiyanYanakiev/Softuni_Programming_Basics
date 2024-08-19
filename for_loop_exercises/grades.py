students_total = int(input())
total_of_grades = 0
fail_amount = 0
between_three_and_three_ninety_nine = 0
between_four_and_four_ninety_nine = 0
top_students_amount = 0

for _ in range(students_total):
    grade = float(input())
    total_of_grades += grade
    if grade < 3:
        fail_amount += 1
    elif grade < 4:
        between_three_and_three_ninety_nine += 1
    elif grade < 5:
        between_four_and_four_ninety_nine += 1
    else:
        top_students_amount += 1

print(f"Top students: {top_students_amount / students_total * 100:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_and_four_ninety_nine / students_total * 100:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_and_three_ninety_nine / students_total * 100:.2f}%")
print(f"Fail: {fail_amount / students_total * 100:.2f}%")
print(f"Average: {total_of_grades / students_total:.2f}")
