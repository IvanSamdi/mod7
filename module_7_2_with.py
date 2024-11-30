def custom_write(file_name, strings):
    n = 0
    elem = {}
    for i in info:
        with open(file_name, 'a', encoding='utf-8') as file:
            tell = (file.tell())
            n += 1
            file.write(f'{i}\n')
            elem.update({(n, tell): i})
    return elem


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test1.txt', info)
for elem in result.items():
    print(elem)
