rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('File4_ru.txt', 'w', encoding='utf-8') as new_perf:
    with open('text_4.txt', encoding='utf-8') as perf:
        new_perf.writelines([line.replace(line.split()[0], rus.get(line.split()[0])) for line in perf])