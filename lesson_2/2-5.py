my_list = [7, 5, 3, 3, 2]

user_number = float(input('Введите число от 0 до 100: '))
i = 0
for n in my_list:
    if user_number <= n:
        i += 1
    else:
        break

my_list.insert(i, user_number)
print(my_list)