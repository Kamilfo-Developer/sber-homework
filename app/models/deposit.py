import datetime
from datetime import date

from pydantic import BaseModel, field_validator


class Deposit(BaseModel):
    date: date

    @field_validator("date", mode="before")
    def validate_date(cls, value) -> datetime.date:
        # Used to handle string input from FastAPI
        if isinstance(value, str):
            datetime_value = datetime.datetime.strptime(value, "%d.%m.%Y")

            return datetime.date(
                datetime_value.year, datetime_value.month, datetime_value.day
            )

        if isinstance(value, datetime.date):
            return value

        raise ValueError(
            "Value should be either datetime.date or string in format dd.mm.yyyy",
        )

    periods: int

    @field_validator("periods")
    def validate_periods(cls, value: int) -> int:
        value_in_range_from_1_to_60 = 1 <= value <= 60

        if not value_in_range_from_1_to_60:
            raise ValueError(
                "periods value must be in range [1, 60]",
            )

        return value

    amount: int

    @field_validator("amount")
    def validate_amount(cls, value: int) -> int:
        value_in_range_from_10000_to_3000000 = 10_000 <= value <= 3_000_000

        if not value_in_range_from_10000_to_3000000:
            raise ValueError(
                "amount must be in range [10 000, 3 000 000]",
            )

        return value

    rate: float

    @field_validator("rate")
    def validate_rate(cls, value: float) -> float:
        value_in_range_from_1_to_8 = 1 <= value <= 8

        if not value_in_range_from_1_to_8:
            raise ValueError(
                "raites must be in range [1, 8]",
            )

        return value
