import telebot

import buttons
bot = telebot.TeleBot('6893734357:AAGPMGm97n5bKnS6q3YgHWvUcfLnmlUleQw')
@bot.message_handler(commands=["start"])
def start(message):
    global uid
    uid=message.from_user.id
    bot.send_message(uid,"Добро пожаловать в наш бот",reply_markup=buttons.menu())

@bot.message_handler(content_types=['text'])
def start_mybot(message):
    if message.text == 'Заказать услугу':
        bot.send_message(uid, 'Отправьте свое имя', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")

def get_name(message):
    user_name = message.text
    print(user_name)
    bot.send_message(uid, 'Отлично, отправьте номер телефона',reply_markup=buttons.number_button())
    bot.register_next_step_handler(message, get_number,user_name)

def get_number(message,user_name):
    if message.contact and message.contact.phone_number:
        user_number = message.contact.phone_number
        bot.send_message(uid, "Выберите услугу", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_service, user_name, user_number)
    else:
        bot.send_message(uid,"Отправьте номер спомощью кнопки")
        #отправляем пользователя обратно
        bot.register_next_step_handler(message,get_number,user_name)
def get_service(message,user_name,user_number):
    user_service = message.text
    bot.send_message(uid, "Какой срок?")
    bot.register_next_step_handler(message,user_number,user_name,user_service)



bot.infinity_polling()