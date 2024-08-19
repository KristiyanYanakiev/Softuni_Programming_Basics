days_off = int(input())

MINUTES_PER_DAY_WHEN_ON_WORK = 63
MINUTES_PER_DAY_ON_DAYS_OFF = 127

working_days = 365 - days_off

total_minutes_a_year = working_days * MINUTES_PER_DAY_WHEN_ON_WORK + days_off * MINUTES_PER_DAY_ON_DAYS_OFF

dif_hours_if_above_norme = (total_minutes_a_year - 30000) // 60
dif_minutes_if_above_norme = (total_minutes_a_year - 30000) % 60

dif_hours_if_below_norme = (30000 - total_minutes_a_year) // 60
dif_miinutes_if_below_norme = (30000 - total_minutes_a_year) % 60


if total_minutes_a_year > 30000:
    print("Tom will run away")
    print(f"{dif_hours_if_above_norme} hours and {dif_minutes_if_above_norme} minutes more for play")

elif total_minutes_a_year < 30000:
    print(f"Tom sleeps well")
    print(f"{dif_hours_if_below_norme} hours and {dif_miinutes_if_below_norme} minutes less for play")

