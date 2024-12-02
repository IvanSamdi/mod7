class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = tuple(file_names)

    def get_all_words(self):
        all_words = {}
        for next_file in self.file_names:
            with open(next_file, 'r', encoding='utf-8') as file:
                next_string = file.read().lower()
                for i in next_string:
                    if i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        next_string = next_string.replace(i, '')
                    elif i == '\n':
                        next_string = next_string.replace(i, " ")
                all_words[next_file] = next_string.split(' ')
        return all_words

    def find(self, word):
        dict_file_number = {}
        for name, words in self.get_all_words().items():

            number_word = 0
            for i in words:
                if word.lower() == words[number_word].lower():
                    dict_file_number[name] = number_word + 1
                else:
                    number_word += 1
        return dict_file_number

    def count(self, word):
        dict_file_count = {}
        for name, words in self.get_all_words().items():
            count_word = 0
            for i in words:
                if word.lower() == i.lower():
                    count_word += 1
            dict_file_count[name] = count_word
        return dict_file_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
