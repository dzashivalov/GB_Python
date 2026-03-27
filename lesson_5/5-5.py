def summary():
    try:
        with open('file5_5.txt', 'w+') as perf:
            line = input('Введите цифры через пробел \n')
            perf.writelines(line)
            my_numbers = line.split()

            print(sum(map(int, my_numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Некорректные данные!')


summary()