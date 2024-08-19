exam_hour = int(input())
exam_minutes = int(input())
student_hour = int(input())
student_minutes = int(input())

total_exam_minutes = exam_hour * 60 + exam_minutes
total_student_minutes = student_hour * 60 + student_minutes
hours = 0
time_dif = total_exam_minutes - total_student_minutes

if total_student_minutes > total_exam_minutes:
    print("Late")
elif total_exam_minutes - total_student_minutes <= 30:
    print("On time")
else:
    print("Early")

if 0 < time_dif <= 59:
    print(f"{time_dif} minutes before the start")
elif 0 < time_dif >= 59:
    hours = time_dif // 60
    minutes = time_dif % 60
    print(f"{hours}:{minutes:02d} hours before the start")

if 0 < total_student_minutes - total_exam_minutes <= 59:
    print(f"{total_student_minutes - total_exam_minutes} minutes after the start")
elif 0 < total_student_minutes - total_exam_minutes > 59:
    hours = (total_student_minutes - total_exam_minutes) // 60
    minutes = (total_student_minutes - total_exam_minutes) % 60
    print(f"{hours}:{minutes:02d} hours after the start")
