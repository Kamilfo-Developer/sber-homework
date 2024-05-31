import datetime

from utils.get_month_with_last_day_date import get_month_with_last_day_date


def test_returns_current_month_last_day_date():
    assert get_month_with_last_day_date(
        date=datetime.date(2021, 1, 30)
    ) == datetime.date(2021, 1, 31)


def test_last_month_day_correctly_returns_last_day_when_leap_day():
    assert get_month_with_last_day_date(
        date=datetime.date(2016, 2, 27)
    ) == datetime.date(2016, 2, 29)


def test_last_month_day_correctly_returns_last_day_when_not_leap_day():
    assert get_month_with_last_day_date(
        date=datetime.date(2017, 2, 25)
    ) == datetime.date(2017, 2, 28)


def test_last_month_day_correctly_returns_last_day_when_end_of_year():
    assert get_month_with_last_day_date(
        date=datetime.date(2017, 12, 30)
    ) == datetime.date(2017, 12, 31)
