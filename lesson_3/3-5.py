def my_sum():
    sum_result = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел, для выхода нажмите Q: ').split()
        result = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                ex = True
                return sum_result
            else:
                result = result + int(number[i])
        sum_result = sum_result + result
        print(f'Сумма чисел равна: {sum_result}')


my_sum()
