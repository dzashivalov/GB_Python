with open('text_6.txt', 'r', encoding='utf-8') as perf:
    print({string.split(':')[0]: sum([int(s[:s.index('(')]) for s in string.split() if '(' in s]) for string in perf})
