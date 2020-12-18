import random
import telebot
bot = telebot.TeleBot('1323964128:AAHAluGjcuNeAGGpiBEOdWOYvx-46l1Qqyc')
import sqlite3
conn = sqlite3.connect('C:\\Users\\Анастасия\\Desktop\\бт\\bot.db')
cursor = conn.cursor()
from telebot import types
from sqlite3 import Error
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Привет {message.from_user.first_name}! \n Если хочешь узнать свой гороскоп напиши: гороскоп.',
                     parse_mode='html')
    print(message)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	# Если написали «Гороскоп»
	if message.text == 'гороскоп' or message.text ==  'Гороскоп' :
		# Пишем приветствие
		bot.send_message(message.from_user.id, "сейчас я расскажу тебе гороскоп на сегодня.")
		# Готовим кнопки
		keyboard = types.InlineKeyboardMarkup()
		# По очереди готовим текст и обработчик для каждого знака зодиака
		key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac Овен')
		# И добавляем кнопку на экран
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
		# Показываем все кнопки сразу и пишем сообщение о выборе
		bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
	elif message.text == "/help":
			bot.send_message(message.from_user.id, "Напиши слово: Гороскоп")
	else:
				bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)

   
def callback_worker(call):
   
    data = call.data.split(" ")
    command = data[0]

    sign = data[1]
    
    if command == "zodiac":
     with sqlite3.connect('C:\\Users\\Анастасия\\Desktop\\бт\\bot.db') as connection:
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
