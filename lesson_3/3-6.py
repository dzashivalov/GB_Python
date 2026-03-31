# Первый вариант
def func(a):
    return a.title()


print(func("hello world"))


# Второй вариант

def int_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


print(int_func("hello world"))
