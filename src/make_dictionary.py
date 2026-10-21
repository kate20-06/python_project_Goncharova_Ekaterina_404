from MissedLetter import MissedLetter
from MissedLetter import MisLetTopic2
def make_right_word(word):
    word = word.replace(',','')
    word = word.replace(' ','')
    word = word.replace('.','')
    word = word.replace('ё','е')
    return word

def MakeDict1(file_name1, file_name2):
    '''
    Функция для создания словаря topic1
    в каждой ячейке хранятся значения класса MissedLetter
    Значения ячеек берутся из файлов file_name1, file_name2
    '''
    dic = open(file_name1, encoding='utf-8')
    dictionary = []
    for i in dic:
        number_of_words = i.split()
        for j in number_of_words:
            dictionary.append(MissedLetter(make_right_word(j), ''))
    dic.close()
    dic = open(file_name2, encoding='utf-8')
    num_word = 0
    for i in dic:
        number_of_words = i.split()
        for j in number_of_words:
            dictionary[num_word].correct_spelling = make_right_word(j)  
            num_word += 1     
    dic.close()
    return dictionary

def MakeDict3(file_name1, file_name2):
    '''
    Функция для создания словаря topic3
    в каждой ячейке хранятся значения класса MissedLetter
    Значения ячеек берутся из файлов file_name1, file_name2
    '''
    dic = open(file_name1, encoding='utf-8')
    dictionary = []
    for i in dic:
        dictionary.append(MissedLetter(i[:-1], ''))
    dic.close()
    dic = open(file_name2, encoding='utf-8')
    num_word = 0
    for i in dic:
        dictionary[num_word].correct_spelling = i[:-1]  
        num_word += 1     
    dic.close()
    return dictionary

def MakeDict2(file_name1, file_name2, file_name3):
    '''
    Функция для создания словаря topic2
    в каждой ячейке хранятся значения класса MisLetTopic2
    Значения ячеек берутся из файлов file_name1, file_name2, file_name3
    '''
    dic = open(file_name1, encoding='utf-8')
    dictionary = []
    for i in dic:
        dictionary.append(MisLetTopic2(i[:-1], '', ''))
    dic.close()
    dic = open(file_name2, encoding='utf-8')
    num_word = 0
    for i in dic:
        dictionary[num_word].correct_spelling = i[:-1]  
        num_word += 1     
    dic.close()
    dic = open(file_name3, encoding='utf-8')
    num_word = 0
    for i in dic:
        dictionary[num_word].missing_letter = i[:-1]  
        num_word += 1     
    dic.close()
    return dictionary

def MakeDict4(file_name1, file_name2):
    '''
    Функция для создания словаря topic4
    в каждой ячейке хранятся значения класса MissedLetter
    Значения ячеек берутся из файлов file_name1, file_name2
    '''
    dic = open(file_name1, encoding='utf-8')
    dictionary = []
    for i in dic:
        dictionary.append(MissedLetter(i[:-1], 'yes'))
    dic.close()

    dic = open(file_name2, encoding='utf-8')
    for i in dic:
        dictionary.append(MissedLetter(i[:-1], 'no'))
    dic.close()
    
    return dictionary