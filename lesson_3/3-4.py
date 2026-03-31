# Оператор **
def my_func(x, y):
    if y >= 0:
        print("Введите целое отрицательное число. Выход из программы.")
        exit()
    return x ** y


a = float(input("Основание. Введите число больше нуля: "))
b = int(input("Степень. Введите целое отрицательное число: "))
print(my_func(a, b))


# Цикл while
def my_func(x, y):
    y = abs(y)
    i = 1
    c = int()
    while i <= y - 1:
        if i > 1:
            c = c * x
        else:
            c = x * x
        if i == (y - 1):
            return 1 / c
        i += 1


a = float(input("Основание. Введите число больше нуля: "))
b = int(input("Степень. Введите целое отрицательное число: "))
print(my_func(a, b))
