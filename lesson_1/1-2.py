seconds = int(input("Введите время в секундах: "))
hours = seconds / 3600
minutes = seconds / 60
print(f'Время в формате ч:м:с - {hours:.1f} : {minutes:.1f} : {seconds}')
