from itertools import count

for el in count(int(input('Введите стартовое число: '))):
    print(el)
    if el >= 10:
        break


from itertools import cycle

c = 0
my_list = [123, False, 'XXX', None]
for el in cycle(my_list):
    print(el)
    c += 1
    if c >= 10:
        break
