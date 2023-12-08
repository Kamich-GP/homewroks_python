import telebot
from telebot import types
from currency_converter import CurrencyConverter

bot = telebot.TeleBot("6963068174:AAEXPchoby5GhnUtc4GNiEcu-SfXdX9sEAg")

Currency = CurrencyConverter()

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Введите сумму для конвертации:")

@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    try:
        amount = float(message.text)
        keyboard = types.ReplyKeyboardMarkup(row_width=3)
        b1 = types.KeyboardButton("RUB/USD")
        b10 = types.KeyboardButton("RUB/EUR")
        b2 = types.KeyboardButton("USD/EUR")
        b20 = types.KeyboardButton("USD/RUB")
        b3 = types.KeyboardButton("EUR/USD")
        b30 = types.KeyboardButton("EUR/RUB")
        keyboard.add(b1,b10,b2,b20,b3,b30)
        bot.send_message(message.chat.id, "Выберите кнопку для конвертации:", reply_markup=keyboard)
        bot.register_next_step_handler(message, process_currency_selection, amount)
    except ValueError:
        bot.send_message(message.chat.id, "Введите корректное число для конвертации")

def process_currency_selection(message, summ):
    admin = message.text
    result = 0

    try:
        if admin == "RUB/USD":
            result = Currency.convert(summ, 'RUB', 'USD')
        elif admin == "RUB/EUR":
            result = Currency.convert(summ, 'RUB', 'EUR')
        elif admin == "USD/EUR":
            result = Currency.convert(summ, 'USD', 'EUR')
        elif admin == "USD/RUB":
            result = Currency.convert(summ, 'USD', 'RUB')
        elif admin == "EUR/USD":
            result = Currency.convert(summ, 'EUR', 'USD')
        elif admin == "EUR/RUB":
            result = Currency.convert(summ, 'EUR', 'RUB')

        if result:
            bot.send_message(message.chat.id, f"Получается: {result:.2f} {admin.split('/')[1]}")
        else:
            bot.send_message(message.chat.id, "Какие-то неполадки:ЗПопробуйте еще раз")
    except ValueError:
        bot.send_message(message.chat.id, "Какие-то неполадки:ЗПопробуйте еще раз")

bot.polling()
