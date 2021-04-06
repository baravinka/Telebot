import telebot
bot = telebot.TeleBot('1323964128:AAHAluGjcuNeAGGpiBEOdWOYvx-46l1Qqyc')
import sqlite3

conn = sqlite3.connect('//home//Anastasia56547657//bot1.db')
cursor = conn.cursor()

from telebot import types

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('по знаку зодиака', 'по дате рождения')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, хочешь узнать гороскоп?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'по дате рождения':
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='21.03-20.04',  callback_data='zodiac Овен')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='21.04-21.05', callback_data='zodiac Телец')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='22.05-21.06', callback_data='zodiac Близнецы')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='22.06-22.07', callback_data='zodiac Рак')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='23.07-23.08', callback_data='zodiac Лев')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='24.08-23.09', callback_data='zodiac Дева')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='24.09-23.10', callback_data='zodiac Весы')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='24.10-22.11', callback_data='zodiac Скорпион')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='23.11-22.12', callback_data='zodiac Стрелец')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='23.12-20.01', callback_data='zodiac Козерог')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='21.01-19.02', callback_data='zodiac Водолей')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='20.02-20.03', callback_data='zodiac Рыбы')
        keyboard.add(key_ryby)
        bot.send_message(message.from_user.id, text='Выбери свою дату рождения', reply_markup=keyboard)

    elif message.text.lower() == 'по знаку зодиака':
        bot.send_message(message.from_user.id, "сейчас я расскажу тебе гороскоп на сегодня.")
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac Овен')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac Телец')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac Близнецы')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac Рак')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac Лев')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac Дева')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac Весы')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac Скорпион')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac Стрелец')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac Козерог')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac Водолей')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac Рыбы')
        keyboard.add(key_ryby)
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
            data = call.data.split(" ")
            command = data[0]
            sign = data[1]
            if command == "zodiac":
                with sqlite3.connect('//home//Anastasia56547657//bot1.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("SELECT prediction FROM horoscope WHERE `zodiac sign` = (?)", [sign])
                        data = cursor.fetchone()
                        bot.send_message(call.from_user.id, data)
                        if data is None:
                            return False
                        else:
                            return data

bot.polling(none_stop=True)
conn.close()
