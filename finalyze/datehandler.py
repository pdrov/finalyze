import datetime
import holidays


def is_trading_day(day):
    if day in holidays.US() or datetime.date.weekday(day) >= 5:
        return False
    else:
        return True


def last_n_trading_days(n=5):
    n_days = []
    _day = datetime.date.today()
    for i in range(n):
        if not is_trading_day(_day):
            while not is_trading_day(_day):
                _day -= datetime.timedelta(days=1)
        n_days.append(_day)
        _day -= datetime.timedelta(days=1)
    return n_days


def timestamp():
    return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H-%M-%S-%f")

