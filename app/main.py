from dependencies import get_deposit_calculator
from fastapi import Depends, FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from models.deposit import Deposit
from services.deposit_calculator import DepositCalculator
from settings import APP_SETTINGS

...


client = FastAPI(debug=APP_SETTINGS.DEBUG)


@client.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        # This is literally what the statement of work says, so no quibbles please
        content=({"error": "Описание ошибка"}),
    )


@client.post("/")
async def handle_post(
    deposit: Deposit,
    deposit_calculator: DepositCalculator = Depends(get_deposit_calculator),
):
    return deposit_calculator.calculate(deposit)
