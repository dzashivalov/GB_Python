with open('File5_1.txt', 'w', encoding='utf-8') as perf:
    while True:
        line = input('введите текст, для окончания ввода оставте пустую строку: ')
        if not line:
            break
        print(line, file=perf)