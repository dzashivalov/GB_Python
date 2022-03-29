num = int(input('Введите целое положительное число: '))
while num < 0:
    n = int(input("Введите число больше нуля: "))

last = num % 10  # Определяем последнюю цифру
num = num // 10  # Все цифры до последней
while num > 0:
    if num % 10 > last:
        last = num % 10
        print(num)
    num = num // 10
print(f'Самая большая цифра в числе: {last}')
