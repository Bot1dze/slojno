from aiogram.filters.callback_data import CallbackData


class WorkDayCallback(CallbackData, prefix='work_day'):
    time: str
    day: str