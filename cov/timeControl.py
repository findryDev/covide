import datetime as dt
import pytz

IST = pytz.timezone('Europe/Warsaw')


def waitTo(hour: int):
    i = dt.datetime(hour=hour, minute=0, second=0,
                    year=dt.datetime.now(IST).year,
                    month=dt.datetime.now(IST).month,
                    day=dt.datetime.now(IST).day) + dt.timedelta(days=1)
    return (int((i - dt.datetime.now(IST)).total_seconds()))
