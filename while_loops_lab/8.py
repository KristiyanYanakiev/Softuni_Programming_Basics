student_name = input()

fail_counter = 0
grade_counter = 0

total_grade = 0

for _ in range(1,13):
    current_grade = float(input())
    grade_counter += 1
    total_grade += current_grade

    if current_grade < 4.0:
        fail_counter += 1

    if fail_counter > 1:
        print(f"{student_name} has been excluded at {grade_counter - 1} grade")

else:
    print(f"{student_name} graduated. Average grade: {total_grade / 12:.2f}")

