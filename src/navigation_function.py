import telebot
from telebot import types
bot = telebot.TeleBot('6176176935:AAGhvGBt18ng0n_PtaA2g4InmvGFfG9LAZI')

def help(message):    
    bot.send_message(message.chat.id, 'Наш бот создан для '
        'отработки подготовки к ЕГЭ по русскому языку', parse_mode='html')
    
    bot.send_message(message.chat.id, 'Введите /go и выберите тему, которую хотите отработать', parse_mode='html')
    
    bot.send_message(message.chat.id, 'Введите /give_rules, чтобы получить материалы с правильными ответами', parse_mode='html')
    
    bot.send_message(message.chat.id, 'Чтобы начать или '
        'закончить практику, можно воспользоваться '
        'меню(командами /go и /stop соответсвенно)',
         parse_mode='html')
   
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    go = types.KeyboardButton('/go')
    stop = types.KeyboardButton('/stop')
    help = types.KeyboardButton('/help')
    give_rules = types.KeyboardButton('/give_rules')
    mess = f'Привет, {message.from_user.first_name}.'
    markup.add(go, stop, help, give_rules)
    bot.send_message(message.chat.id, mess, reply_markup=markup)
    bot.send_message(message.chat.id, 'Нажмите /help, чтобы узнать, '
        'как пользоваться ботом', reply_markup=markup)

