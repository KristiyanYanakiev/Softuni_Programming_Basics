from math import ceil


name_tv_show = str(input())
time_per_episode = int(input())
time_break = int(input())

lunch_time = time_break / 8
leisure_time = time_break / 4

time_left = time_break - (lunch_time + leisure_time)

if time_left >= time_per_episode:
    print(f"You have enough time to watch {name_tv_show} and left with {ceil(time_left - time_per_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_tv_show}, you need {ceil(time_per_episode - time_left)} more minutes.")

