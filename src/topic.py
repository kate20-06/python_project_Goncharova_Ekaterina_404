import telebot
from telebot import types
import make_dictionary
from random import randint
bot = telebot.TeleBot('6176176935:AAGhvGBt18ng0n_PtaA2g4InmvGFfG9LAZI')

class Topic:
    '''
    Класс является словарем для конкретного топика
    Принимает в себя файлы с правильным написанием и пропущенными буквами
    Принимает праввила использования топика
    '''
    dictionary = []
    len_dic = 0
    users_progress = dict()
    rules_of_topic = ''
    rules = ''
    errors = dict()

    def __init__(self, name_file1, name_file2, t_ru):
        self.dictionary = make_dictionary.MakeDict1(name_file1, name_file2)
        self.len_dic = len(self.dictionary)
        self.rules_of_topic= t_ru
        self.rules = name_file2

    def get_task(self, message):
        '''
        Функция дает пользователю задание и проверяет его правильность
        '''
        Id = message.chat.id
        if (self.users_progress[Id])[1] == self.len_dic:
            bot.send_message(message.chat.id, f'Слова закончились, молодец, '
                             f'у тебя {self.errors[Id]} ошибок')
        else:
            if (self.dictionary[(self.users_progress[Id])[0]]).correctness_answer(message.text):
                bot.send_message(message.chat.id, 'good')
            else:
                bot.send_message(message.chat.id, f'ошибка, '
                  f'правильно: {self.dictionary[(self.users_progress[Id])[0]].correct_spelling}')
                self.errors[Id] += 1
            (self.users_progress[Id])[(self.users_progress[Id])[0] + 2] = 1
            (self.users_progress[Id])[1] += 1
            while (self.users_progress[Id]) [(self.users_progress[Id])[0] + 2] == 1:
                (self.users_progress[Id])[0] = randint(0, self.len_dic - 1)
            bot.send_message(message.chat.id,
                            (self.dictionary[(self.users_progress[Id])[0]]).word_with_missing_letter)

    def go(self, callback):
        '''
        Начало работы топика
        '''
        Id = (callback).from_user.id
        self.errors[Id] = 0
        now_ind = randint(0, self.len_dic - 1)
        self.users_progress[Id] = [now_ind] + [0] + [0] * self.len_dic
        bot.send_message(callback.message.chat.id,
                         (self.dictionary[now_ind]).word_with_missing_letter)
    def get_rules_of_topic(self, callback):
        '''
        Вывести правила топика
        '''
        bot.send_message(callback.message.chat.id, self.rules_of_topic)

    def get_rules(self, callback):
        '''
        Вывести файл с правильным написанием слов
        '''
        with open(self.rules, 'rb') as f:
            file = f.read()
        bot.send_document(callback.message.chat.id, document = file)

class Topic3(Topic):
    '''
    класс для третьего топика
    '''
    def __init__(self, name_file1, name_file2, t_ru):
        self.dictionary = make_dictionary.MakeDict3(name_file1, name_file2)
        self.len_dic = len(self.dictionary)
        self.rules_of_topic= t_ru
        self.rules = name_file2

class Topic2(Topic):
    '''
    класс для второго топика
    '''
    def __init__(self, name_file1, name_file2, name_file3, t_ru):
        self.dictionary = make_dictionary.MakeDict2(name_file1, name_file2, name_file3)
        self.len_dic = len(self.dictionary)
        self.rules_of_topic= t_ru
        self.rules = name_file2

class Topic4(Topic):
    '''
    класс для четвертого топика
    '''
    def __init__(self, name_file1, name_file2, t_ru):
        self.dictionary = make_dictionary.MakeDict4(name_file1, name_file2)
        self.len_dic = len(self.dictionary)
        self.rules_of_topic= t_ru
        self.rules = name_file2