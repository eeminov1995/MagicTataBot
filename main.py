from secrets import token  # Импортим токен
import telebot  # Шоб бот вообще работал
from telebot import types  # Шоб работать с кнопками
import random  # Шоб бот рандомные ответы давал из списка
import datetime  # Шоб время принтить в лог
import json  # Шоб суетить Джейсона Стетхема
import os  # Шоб дёргать из ФС Джейсона

# Инициализируем бот и импортим токен
bot = telebot.TeleBot(token)

# Глобальные переменне
answer_tmp = None
user = None

# Функция для загрузки списка ответов из файла
def load_answers():
    if os.path.exists('answers.json'):
        with open('answers.json', 'r') as file:
            return json.load(file)
    else:
        return [
    "Да",
    "Нет",
    "Убедись, что у тебя есть запасные трусики, жизнь — непредсказуема!",
    "Да, и не забудь купить лотерейный билет — удача на твоей стороне!",
    "Не думаю",
    "Да, и помни: твоя улыбка — залог успеха!",
    "Нет, но ты можешь попытаться угостить меня пирожными…",
    "У меня к тебе тот же вопрос.",
    "Да, и не забудь: королевская воля — закон!",
    "Нет, и я не собираюсь менять свое решение без веских на то причин!",
    "Маловероятно",
    "Да, но только после того, как ты сделаешь мне чашечку чая!",
    "Скорее нет, чем да, но у меня есть план Б — чипсы Pringles со вкусом сметаны и лука!",
    "Наверное",
    "Определенно нет! Я не одобряю такие глупости.",
    "Да, GPS на твоей карете уже прокладывает маршрут к успеху.",
    "Нет, но ты можешь попробовать меня уговорить…",
    "Не стоит",
    "Да, и я уже предвкушаю, как это будет… интересно!",
    "Нет, но если ты найдешь волшебную палочку, я помогу!",
    "Спроси снова, когда я не буду занят просмотром сериалов!",
    "Разумеется, но сначала отряхни свои туфельки — королевский порядок!",
    "Нет, но я могу рассмотреть альтернативные варианты с десертом!",
    "Ни в коем случае",
    "Скорее всего! Но я бы на твоем месте не ставил на одну лошадку… или на одного бота.",
    "Нет, и это не обсуждается! Я не готов к такому уровню ответственности…",
    "Сомневаюсь",
    "Безусловно, но пожалуйста, не забывай о манерах!",
    "Нет, и я настоятельно рекомендую тебе подумать дважды!",
    "Конечно! Но только если ты сделаешь это с изяществом…",
    "Нет! Я не потерплю легкомысленных предложений, если это не касается…",
    "Да, и я готов к приключениям… в твоем исполнении!",
    "Нет и не пытайся меня соблазнить своими уловками!",
    "Определенно да! Я всегда готов к приключениям с тобой!",
    "Нет, но если ты предложишь что-то более интригующее, я подумаю!",
    "Наверное",
    "Нет, и даже не думай об этом без моего согласия!",
    "Моя дорогая, твое будущее полно загадок и недопитых чашек кофе…",
    "Да, если ты готова к приключениям или к очередному сериалу!",
    "Нет, но я могу предложить альтернативный вариант — суши!",
    "Да, если ты будешь смеяться над моими шутками!",
    "Нет, но это не значит, что ты не можешь попробовать… завтра!"
    ]

# Функция для сохранения списка ответов в файл
def save_answers(answers):
    with open('answers.json', 'w') as file:
        json.dump(answers, file)

# Загрузка списка ответов при запуске бота, если виртуалка заруинилась
answers = load_answers()

# Первая команда
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я магический шар для Таты Апполоновой')

# Служебная команда для очистки лога запросов
@bot.message_handler(commands=['log'])
def clean_log(message):
    with open('log.txt', 'w') as file:
            file.write('')

# Обрабатываем онли текст
@bot.message_handler(content_types=['text'])
def button(message):
    global answer_tmp
    answer_tmp = random.choice(answers)  # Сохраняем ответ, шоб можно было его обрабатывать
    markup = types.InlineKeyboardMarkup()  # Инициализируем управлялку кнопками
    bt_show = types.InlineKeyboardButton('Вывести список', callback_data='show_list')  # Кнопка 1
    bt_edit = types.InlineKeyboardButton('Изменить этот ответ', callback_data='edit_answer')  # Кнопка 2
    bt_del = types.InlineKeyboardButton('Удалить этот ответ', callback_data='del_answer')  # Кнопка 3
    markup.add(bt_show)  # Пихаем кнопки в управлялку
    markup.add(bt_edit)  # Пихаем кнопки в управлялку
    markup.add(bt_del)  # Пихаем кнопки в управлялку
    bot.send_message(message.chat.id, answer_tmp, reply_markup=markup)  # Отправляем ответ с кнопками

    log_message(message, answer_tmp)  # Логаем запрос

# Определаяем логанье запросов
def log_message(message, answer):
    global user
    user = message.from_user.username
    if len(list(open('log.txt').readlines())) > 1000:
        with open('log.txt', 'w') as file:
            file.write('')
    else:
        with open('log.txt', 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'{timestamp} - {user}: {message.text}\n')
            file.write(f'{timestamp} - Bot: {answer}\n')
            file.write(f'\n')

# Определяем обработку кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'show_list':
        bot.send_message(call.message.chat.id, '\n'.join(answers))
    elif call.data == 'edit_answer':
        if 'appolllllllo' in user or 'moonrhyme_bro' in user:
            bot.send_message(call.message.chat.id, 'Введи новый ответ:')
            bot.register_next_step_handler(call.message, edit_answer)
        else:
            bot.send_message(call.message.chat.id, 'У вас нет прав, пожалуйста, напишите @moonrhyme_bro')
    elif call.data == 'del_answer':
        if answer_tmp in answers and 'appolllllllo' in user or 'moonrhyme_bro' in user:
            answers.remove(answer_tmp)
            save_answers(answers)
            bot.send_message(call.message.chat.id, 'Ответ удалён')
        else:
            bot.send_message(call.message.chat.id, 'У вас нет прав, пожалуйста, напишите @moonrhyme_bro')

# Логика кнопки изменения ответа
def edit_answer(message):
    print(answer_tmp)
    print(user)
    if answer_tmp in answers:
        new_answer = message.text
        index = answers.index(answer_tmp)
        answers[index] = new_answer
        save_answers(answers)
        bot.send_message(message.chat.id, 'Ответ изменён')
    else:
        bot.send_message(message.chat.id, 'Ответ не найден') 

bot.polling(none_stop=True)  # Запускаем ботана