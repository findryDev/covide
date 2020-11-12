import datetime as dt

i = dt.datetime(hour=8, minute=0, second=0, year=dt.datetime.now().year, month=dt.datetime.now().month, day=dt.datetime.now().day) + dt.timedelta(days=1)
print(int((i - dt.datetime.now()).total_seconds()))