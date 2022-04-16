with open('File5_1.txt', 'r', encoding='utf-8') as perf:
    res = [f'{line}. {count.strip()} - {len(count.split())} слова'
           for line, count in enumerate(perf, 1)]
    print(*res, f'Всего строк - {len(res)}.', sep='\n')