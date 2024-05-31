import datetime

from utils.get_next_month_first_day_date import get_next_month_first_day_date


def test_next_month_first_day_returns_next_month_first_day():
    assert get_next_month_first_day_date(
        date=datetime.date(2021, 1, 2)
    ) == datetime.date(2021, 2, 1)


def test_next_month_first_day_correctly_returns_when_leap_year():
    assert get_next_month_first_day_date(
        date=datetime.date(2021, 2, 28)
    ) == datetime.date(2021, 3, 1)


def test_next_month_first_day_correctly_returns_when_not_leap_year():
    assert get_next_month_first_day_date(
        date=datetime.date(2016, 2, 29)
    ) == datetime.date(2016, 3, 1)


def test_next_month_first_day_correctly_returns_when_end_of_year():
    assert get_next_month_first_day_date(
        date=datetime.date(2016, 12, 31)
    ) == datetime.date(2017, 1, 1)
