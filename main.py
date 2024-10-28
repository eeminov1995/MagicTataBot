import telebot
import random

token = '7396766386:AAHNw5jlmgeJxJloSQ3LFbqM0MnDm-qMT2E'
bot = telebot.TeleBot(token)

answers = [
'Да', 
'Возможно', 
'Нет', 
'Сомнительно, но окэй', 
'Канешнаааа', 
'Спроси позже, я ща не хочу отвечать',
'Минестерство магии разрешило не отвечать на такой вопрос', 
'фуууу, нет', 
'ДАААААААААААА', 
'Ни в коем случае',
'Не уверен',
'Ну такое...',
'ДА, но это не точно',
'НЕТ, но это не точно',
'Может быть',
'СТО ПУДОФФФФФ',
'А вот нихренаааа... нихренашеньки',
'Полюбэ',
'Спроси у гугла',
'Это не в моих компетенциях','Не сегодня, не сейчас, но скоро!',
'Всё зависит от тебя!',
'Иногда банан — это просто банан!',
'Да и точка',
'Наверное и точка',
'Нет и точка',
'А почему бы и нет?',
]

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, я магический шар для Таты Апполоновой')

@bot.message_handler()
def questions(message):
    bot.send_message(message.chat.id, f'{random.choice(answers)}')

bot.polling(none_stop=True)