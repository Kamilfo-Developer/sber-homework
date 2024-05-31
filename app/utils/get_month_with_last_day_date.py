import datetime


def get_month_with_last_day_date(date: datetime.date):
    nxt_mnth = date.replace(day=28) + datetime.timedelta(days=4)

    return nxt_mnth - datetime.timedelta(days=nxt_mnth.day)
