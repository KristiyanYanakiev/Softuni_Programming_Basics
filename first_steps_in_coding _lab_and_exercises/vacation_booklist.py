number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

total_time_needed = number_of_pages // pages_per_hour
pages_a_day = total_time_needed // number_of_days

print(pages_a_day)

