def my_func(arg1, arg2):
    try:
        result = arg1 / arg2
        return result
    except ZeroDivisionError:
        return "На ноль делить нельзя"


first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))
print(my_func(first_num, second_num))
