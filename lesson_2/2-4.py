user_str = list(input('Введети строку из нескольких слов, разделённых пробелами: ').split())

for i in range(len(user_str)):
    print(i + 1, ')', user_str[i][:10])