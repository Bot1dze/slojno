from aiogram import Router
from aiogram.types import CallbackQuery

from callbacks.Work_Day_callback import WorkDayCallback

work_router = Router()


@work_router.callback_query(WorkDayCallback.filter())
async def handle_waifu_type(query: CallbackQuery, callback_data: WorkDayCallback):
    if callback_data.time == 'work':
        await query.message.answer('Используя /work напиши своё расписание\n(пример: /work 10 00 14 30)')
    else:
        await query.message.answer('Выходные прекрасны, не так ли?')