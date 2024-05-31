import datetime

from models.deposit import Deposit
from utils.get_next_month_first_day_date import get_next_month_first_day_date


class DepositCalculator:
    def __init__(self):
        pass

    def __calculate_for_month(
        self, initial_amount: int, rate: float, period: int
    ) -> float:
        result = initial_amount * (1 + (rate / 100) / 12) ** period

        DECIMAL_ACCURACY = 100

        rounded_result = round(result * DECIMAL_ACCURACY) / DECIMAL_ACCURACY

        return rounded_result

    def __get_next_month_key(self, current_date: datetime.date) -> str:
        nxt_mnth = current_date.replace(day=28) + datetime.timedelta(days=4)

        result = nxt_mnth - datetime.timedelta(days=nxt_mnth.day)

        return result.strftime("%d.%m.%Y")

    def calculate(self, deposit: Deposit):
        result: dict[str, float] = {}

        current_date = deposit.date

        for period in range(1, deposit.periods + 1):
            result[self.__get_next_month_key(current_date)] = (
                self.__calculate_for_month(
                    deposit.amount, deposit.rate, period
                )
            )

            current_date = get_next_month_first_day_date(current_date)

        return result
