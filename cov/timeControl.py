import datetime as dt
import pytz


def waitTo(hour: int):
    IST = pytz.timezone('Europe/Warsaw')
    now = dt.datetime.now(IST)
    i = dt.datetime(hour=hour, minute=0, second=0,
                    year=dt.datetime.now().year,
                    month=dt.datetime.now().month,
                    day=dt.datetime.now().day) + dt.timedelta(days=1)
    i = pytz.timezone('Europe/Warsaw').localize(i)
    return (int((i - now).total_seconds()))
