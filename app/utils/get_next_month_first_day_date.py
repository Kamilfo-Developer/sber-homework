import datetime


def get_next_month_first_day_date(date: datetime.date) -> datetime.date:
    dt_new = (date.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)

    return dt_new
