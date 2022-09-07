# https://www.codewars.com/kata/5837fd7d44ff282acd000157/train/python
import datetime

def count_days(d):
    date = datetime.date(d.year, d.month, d.day)
    now = datetime.date.today()
    if date == now:
        return "Today is the day!"
    elif date < now:
        return "The day is in the past!"
    else:
        return f'{(date - now).days} days'


