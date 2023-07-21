from work_calendar_ru import WCR
from aiogram import Router

from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from States.schedule import ScheduleStatesGroup
from keyboards.inline import work_days_keyboard
import datetime

common_router = Router()

from Data.schedule_data import schedule


@common_router.message(Command('start'))
async def start_command(message: Message):
    await message.answer('Какой сегодня день недели?', reply_markup=work_days_keyboard)


@common_router.message(Command('work'))
async def work_command(message: Message):
    user_id = message.chat.id
    day = datetime.datetime.now().weekday()
    all_days = schedule.get(user_id)
    if all_days is None:
        await message.answer('Заведите расписание через /set_work')
    else:
        current_day = all_days.get(day)
        if current_day is None:
            await  message.answer('Этого дня нет в расписании')
        else:
            if current_day.is_work_time():
                await message.answer('Работаем')
            else:
                await message.answer('Отдыхаем')


@common_router.message(Command('timing'))
async def timing_command(message: Message):
    day = datetime.datetime.now().weekday()
    user_id = message.chat.id
    a = schedule.get(user_id)
    if a is None:
        await message.answer('У вас ещё нет расписания')
    else:
        current_user_wcr = a.get(day)
        if current_user_wcr is None:
            await message.answer('У вас нет расписания на этот день')
        else:
            if current_user_wcr.is_work_time():
                await message.answer('Работаем')
            else:
                await message.answer('Отдыхаем')


@common_router.message(Command('set_work'))
async def set_work_command(message: Message, state: FSMContext):
    arguments = message.text.split()[1:]
    if len(arguments) == 1 and arguments[0].isdigit() and 1 <= int(arguments[0]) <= 7:
        await message.answer('Введите числа: Начало в часах, минута, конец в часах, минутах')
        await state.update_data(day=int(arguments[0]))
        await state.set_state(ScheduleStatesGroup.fill_day_schedule)
    else:
        await message.answer('Надо ввести одно целое число от 1 до 7')


@common_router.message(StateFilter(ScheduleStatesGroup.fill_day_schedule))
async def set_schedule(message: Message, state: FSMContext):
    user_id = message.chat.id
    arguments = message.text.split()
    start_hour = int(arguments[0])
    start_minute = int(arguments[1])
    end_hour = int(arguments[2])
    end_minute = int(arguments[3])
    state_data = await state.get_data()
    wcr = WCR(start_hour, start_minute, end_hour, end_minute)
    if schedule.get(user_id) is None:
        schedule[user_id] = {
            state_data['day']: wcr
        }
    else:
        schedule[user_id][state_data['day']] = wcr
    await state.clear()


@common_router.message(Command(commands=['timing']))
async def get_timing(message: Message):
    current_user_stats = schedule[message.chat.id]
    await message.answer(f'Твой график:\nНачало в {current_user_stats["start_hour"]} {current_user_stats["start_minute"]}\nОкончание в {current_user_stats["end_hour"]} {current_user_stats["end_minute"]}')
