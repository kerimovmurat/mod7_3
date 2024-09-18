class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='cp1251') as file:
                content = file.read().lower() # cодержимое файла читается и преобразуется в нижний регистр для унификации
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']: # цикл проходит по списку знаков препинания
                    content = content.replace(punct, '') #   метод replace заменяет все вхождения строки punct на пустую строку ''
                words = content.split() # метода split() # cодержимое файла разбивается на отдельные слова
                all_words[file_name] = words # cписок слов добавляется в словарь all_words с именем файла в качестве ключа
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result

# Пример использования класса
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))     # 3 слово по счёту
print(finder2.count('teXT'))    # 4 слова teXT в тексте всего
