from datetime import date

import pytest
from models.deposit import Deposit
from services.deposit_calculator import DepositCalculator


@pytest.fixture
def deposit_calculator() -> DepositCalculator:
    return DepositCalculator()


def test_calculate(deposit_calculator: DepositCalculator) -> None:
    deposit = Deposit(date=date(2021, 1, 31), periods=3, amount=10000, rate=6)

    assert deposit_calculator.calculate(deposit) == {
        "31.01.2021": 10050,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75,
    }
