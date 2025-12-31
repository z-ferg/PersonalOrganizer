from datetime import date
import datetime
import calendar

def get_date():
    d = date.today()

    weekday = d.strftime("%a")

    all_months = list(calendar.month_name)[1:]
    month = all_months[d.month - 1]

    day = d.day

    return f"{weekday}, {month} {day}"