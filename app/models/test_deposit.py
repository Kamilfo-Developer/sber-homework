import datetime

import pytest
from models.deposit import Deposit

VALID_PERIODS = 3
VALID_AMOUNT = 10000
VALID_RATE = 6
VALID_DATE = datetime.date(2021, 1, 31)


def test_deposit_works_correctly_when_string_date():
    try:
        Deposit(
            date="31.01.2021",  # type: ignore
            periods=VALID_PERIODS,
            amount=VALID_AMOUNT,
            rate=VALID_RATE,
        )
    except ValueError:
        pytest.fail("Unexpected ValueError when correct string input")


def test_date_works_correctly_when_datetime_date():
    try:
        Deposit(
            date=datetime.date(2021, 1, 31),
            periods=VALID_PERIODS,
            amount=VALID_AMOUNT,
            rate=VALID_RATE,
        )
    except ValueError:
        pytest.fail("Unexpected ValueError when correct datetime.date input")


def test_deposit_raises_error_when_incorrect_date_format():
    with pytest.raises(ValueError):
        Deposit(
            date="01.31.2021",  # type: ignore
            periods=VALID_PERIODS,
            amount=VALID_AMOUNT,
            rate=VALID_RATE,
        )


def test_deposit_raises_error_when_periods_greater_than_valid_value():
    with pytest.raises(ValueError):
        Deposit(
            date=VALID_DATE,
            periods=70,
            amount=VALID_AMOUNT,
            rate=VALID_RATE,
        )


def test_deposit_raises_error_when_periods_less_than_valid_value():
    with pytest.raises(ValueError):
        Deposit(
            date=VALID_DATE,
            periods=0,
            amount=VALID_AMOUNT,
            rate=VALID_RATE,
        )


def test_deposit_raises_error_when_amount_greater_than_valid_value():
    with pytest.raises(ValueError):
        Deposit(
            date=VALID_DATE,
            periods=VALID_PERIODS,
            amount=3_000_001,
            rate=VALID_RATE,
        )


def test_deposit_raises_error_when_amount_less_than_valid_value():
    with pytest.raises(ValueError):
        Deposit(
            date=VALID_DATE,
            periods=VALID_PERIODS,
            amount=9_999,
            rate=VALID_RATE,
        )


def test_deposit_raises_error_when_rate_greater_than_valid_value():
    with pytest.raises(ValueError):
        Deposit(
            date=VALID_DATE,
            periods=VALID_PERIODS,
            amount=VALID_AMOUNT,
            rate=10,
        )


def test_deposit_raises_error_when_rate_less_than_valid_value():
    with pytest.raises(ValueError):
        Deposit(
            date=VALID_DATE,
            periods=VALID_PERIODS,
            amount=VALID_AMOUNT,
            rate=0,
        )
