with open('text_3.txt', 'r', encoding='utf-8') as perf:
    creeps = {}
    for line in perf:
        creeps[line.split()[0]] = float(line.split()[1])
    print('менее 20к получают:')
for name, creep in creeps.items():
    if creep < 20000:
        print(name)
print(f'средняя з\п равна {sum(creeps.values()) / len(creeps)}')