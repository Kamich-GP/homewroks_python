import telebot

bot = telebot.TeleBot('6648158434:AAGhsXEhAvJqRhB-tvMsZS1DjyfaBKyji6U')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я могу помочь тебе, Наверное:З")

bot.polling()