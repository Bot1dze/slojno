from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks.Work_Day_callback import WorkDayCallback

monday = InlineKeyboardButton(text='Понедельник', callback_data=WorkDayCallback(
    time='work',
    day='monday'
).pack())
tuesday = InlineKeyboardButton(text='Вторник', callback_data=WorkDayCallback(
    time='work',
    day='monday'
).pack())
wednesday = InlineKeyboardButton(text='Среда', callback_data=WorkDayCallback(
    time='work',
    day='monday'
).pack())
thursday = InlineKeyboardButton(text='Четверг', callback_data=WorkDayCallback(
    time='work',
    day='monday'
).pack())
friday = InlineKeyboardButton(text='Пятница', callback_data=WorkDayCallback(
    time='work',
    day='monday'
).pack())
saturday = InlineKeyboardButton(text='Суббота', callback_data=WorkDayCallback(
    time='chill',
    day='saturday'
).pack())
sunday = InlineKeyboardButton(text='Воскресенье', callback_data=WorkDayCallback(
    time='chill',
    day='sunday'
).pack())
work_days_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
])
