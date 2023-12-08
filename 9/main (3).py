import telebot
from telebot import types
import database

bot = telebot.TeleBot('6094401018:AAEe_U93UQzaitwCVwJOAZSDECmdKGOXZOM')

@bot.callback_query_handler(func=lambda callback: True)
def callback_language(callback):
    id = callback.message.chat.id
    if callback.data == 'ru':
        a = callback.message.from_user.id
        bot.send_message(id, "Выбран русский язы.\nВведите свое имя")
        bot.register_next_step_handler(callback.message, get_number_ru, a)
    elif callback.data == 'en':
        a = callback.message.from_user.id
        bot.send_message(id, 'Hi! \nEnter your name')
        bot.register_next_step_handler(callback.message, get_number_en, a)
    elif callback.data == 'uz':
        a = callback.message.from_user.id
        bot.send_message(id, 'Salom! \nIsmingizni yozing')
        bot.register_next_step_handler(callback.message, get_number_uz, a)


@bot.message_handler(commands=['start'])
def button_languages(message):

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Русский', callback_data='ru')
    btn2 = types.InlineKeyboardButton('English', callback_data='en')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Uzbek', callback_data='uz')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Выбирите язык:', reply_markup=markup)

def get_number_en(message, a):
    name = message.text
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Send cntact', request_contact=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Cool! So sent your phone number', reply_markup=markup)
    bot.register_next_step_handler(message, get_geo_en, a, name)


def get_geo_en(message, a, name):
    number = message.text
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Send geo', request_location=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Good!, so send your location',reply_markup=markup)
    bot.register_next_step_handler(message, get_all_data_en, a, name, number)

def get_number_ru(message, a):
    name = message.text
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Отправьте свой номер', request_contact=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Отлично, Теперь отправьте свой номер', reply_markup=markup)
    bot.register_next_step_handler(message, get_geo_ru, a, name)

def get_geo_ru(message, a, name):
    number = message.text
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Отправить геолакацию', request_location=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Отлично!, теперь отправьте свою геолакацию',reply_markup=markup)
    bot.register_next_step_handler(message, get_all_data_ru, a, name, number)

def get_number_uz(message, a):
    name = message.text
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Nomer yuborish', request_contact=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Yaxshi! End telefon raqamingizni yuboring', reply_markup=markup)
    bot.register_next_step_handler(message, get_geo_uz, a, name)

def get_geo_uz(message, a, name):
    number = message.text
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Geolakatsiyani yuborish', request_location=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, 'yaxshi!, endi geolakatsiyazi yuboring',reply_markup=markup)
    bot.register_next_step_handler(message, get_all_data_uz, a, name, number)

def get_all_data_en(message, a, name, number):

    database.add_in_database(a, name, number)
    bot.send_message(message.chat.id, 'Your dates added in database!')

def get_all_data_ru(message, a, name, number):

    database.add_in_database(a, name, number)
    bot.send_message(message.chat.id, 'Ваши данные сохранились в базе данных!')

def get_all_data_uz(message, a, name, number):

    database.add_in_database(a, name, number)
    bot.send_message(message.chat.id, 'Sizning danilariz bazaga saqlandi!!')


bot.infinity_polling()