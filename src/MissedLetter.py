class MissedLetter:
    '''
    Это класс, в котором хранятся слова с пропуском
    и правильное написание этих слов
    '''
    word_with_missing_letter = ''
    correct_spelling = ''
    def __init__(self, word, cor_spel):
        self.word_with_missing_letter = word
        self.correct_spelling = cor_spel
    def correctness_answer(self, user_world):
        '''
        Функция проверки правильности введенного ответа
        '''
        if self.correct_spelling == user_world.lower():
            return True
        return False
class MisLetTopic2(MissedLetter):
    '''
    Атрибут содержащий пропущенную букву
    '''
    missing_letter = ''
    def __init__(self, word, cor_spel, let):
        super().__init__(word, cor_spel)
        self.missing_letter = let
    def correctness_answer(self, user_word):
        if self.missing_letter.lower() == user_word.lower() or (self.correct_spelling).lower() == user_word.lower():
            return True
        return False