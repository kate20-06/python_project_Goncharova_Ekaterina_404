import telebot
from random import *
from telebot import  types
import navigation_function
import topic
import RulesOfBot
from config import token
flag = dict()
bot = telebot.TeleBot(token)
'''
создаем словари для каждого топика
'''
dict_topic1 = topic.Topic('text_files/missedletter.txt', 'text_files/dictionary.txt',
                          RulesOfBot.rules_of_topic1)
dict_topic3 = topic.Topic3('text_files/fused_task.txt', 'text_files/fused_right.txt',
                            RulesOfBot.rules_of_topic2)
dict_topic4 = topic.Topic4('text_files/introductory.txt', 'text_files/not_introductory.txt',
                            RulesOfBot.rules_of_topic4)
dict_topic2 = topic.Topic2('text_files/pre-pri-prop.txt', 'text_files/pre-pri.txt',
                            'text_files/pre-pri_let.txt', RulesOfBot.rules_of_topic3)

@bot.message_handler(commands=['start'])
def start(message):
    navigation_function.start(message)

@bot.message_handler(commands=['help'])
def help(message):    
    navigation_function.help(message)

@bot.message_handler(commands=['stop'])
def stop (message):
    '''
    Завершение работы с топиком и вывод результатов
    '''
    Id = message.from_user.id
    if Id in flag:
        if flag[Id] == 1:
            bot.send_message(message.chat.id, f'У тебя {dict_topic1.errors[Id]} ошибок')
        elif flag[Id] == 2:
            bot.send_message(message.chat.id, f'У тебя {dict_topic2.errors[Id]} ошибок')
        elif flag[Id] == 3:
            bot.send_message(message.chat.id, f'У тебя {dict_topic3.errors[Id]} ошибок')
        elif flag[Id] == 4:
            bot.send_message(message.chat.id, f'У тебя {dict_topic4.errors[Id]} ошибок')
    bot.send_message(message.chat.id, 'Надеюсь наш бот смог тебе помочь',
                      parse_mode='html')
    bot.send_message(message.chat.id, 'До новых встреч', parse_mode='html')
@bot.message_handler(commands=['give_rules'])
def give_rules(message):
    '''
    вывести правила написания слов. возвращает файл
    '''
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('словарные слова',
                                          callback_data = 'topic1_ru')
    button2 = types.InlineKeyboardButton('пре и при', callback_data = 'topic2_ru')
    button3 = types.InlineKeyboardButton('слитное и раздельное написание слов',
                                          callback_data = 'topic3_ru')
    button4 = types.InlineKeyboardButton('вводные и не вводные слова',
                                          callback_data = 'topic4_ru')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    bot.send_message(message.chat.id, 'Выберите тему, '
        'по которой хотите получить файл с правильным написанием', reply_markup = markup)

@bot.message_handler(commands=['go'])
def topic(message):
    '''
    выбор темы и начало работы с топиком
    '''
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('словарные слова',
                                          callback_data = 'topic1')
    button2 = types.InlineKeyboardButton('пре и при', callback_data = 'topic2')
    button3 = types.InlineKeyboardButton('слитное и раздельное написание слов',
                                          callback_data = 'topic3')
    button4 = types.InlineKeyboardButton('вводные и не вводные слова',
                                          callback_data = 'topic4')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    bot.send_message(message.chat.id, 'Выберите тему, '
        'которую хотите отработать', reply_markup = markup)
    Id = message.from_user.id
    flag[Id] = 0

@bot.callback_query_handler()
def callback_message(callback):
    if callback.data == 'topic1_ru':
        dict_topic1.get_rules(callback)
    elif callback.data == 'topic1_ru':
        dict_topic2.get_rules(callback)
    elif callback.data == 'topic3_ru':
        dict_topic3.get_rules(callback)
    elif callback.data == 'topic4_ru':
        dict_topic4.get_rules(callback)
    elif callback.data == 'topic1':
        topic1(callback)
    elif callback.data == 'topic3':
        topic3(callback)
    elif callback.data == 'topic2':
        topic2(callback)
    else:
        topic4(callback)

def topic1(callback):
    dict_topic1.get_rules_of_topic(callback)
    dict_topic1.go(callback)
    Id = callback.from_user.id
    flag[Id] = 1

def topic2(callback):
    dict_topic2.get_rules_of_topic(callback)
    dict_topic2.go(callback)
    Id = callback.from_user.id
    flag[Id] = 2

def topic3(callback):
    dict_topic3.get_rules_of_topic(callback)
    dict_topic3.go(callback)
    Id = callback.from_user.id
    flag[Id] = 3

def topic4(callback):
    dict_topic4.get_rules_of_topic(callback)
    dict_topic4.go(callback)
    Id = callback.from_user.id
    flag[Id] = 4

@bot.message_handler()
def get_user_text(message):
    '''
    запуск выдачи заданий
    '''
    Id = message.from_user.id
    if Id in flag:
        if flag[Id] == 1:
            dict_topic1.get_task(message)
        elif flag[Id] == 3:
            dict_topic3.get_task(message)
        elif flag[Id] == 2:
            dict_topic2.get_task(message)
        else:
            dict_topic4.get_task(message)