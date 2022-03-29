a = int(input("a = "))
b = int(input("b = "))
day = 1
print(f'1-й день: {a}')
while a < b:
    a = a + (a / 100 * 10)
    day = day + 1
    print(f'{day}-й день: {a:.2f}')

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
