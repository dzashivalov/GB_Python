vyr = float(input("Введите выручку фирмы: "))
izd = float(input("Введите издержки фирмы: "))
result = vyr - izd
if result > 0:
    rent = result / vyr
    print(f'Финансовый результат - прибыль. Ее величина: {result:.0f}')
    print(f'Значит вычисляем рентабельность выручки (соотношение прибыли к выручке). '
          f'Рентабельность выручки = {rent}')
    staff = int(input("Введите численность сотрудников фирмы: "))
    staff_result = result / staff
    print(f'Прибыль фирмы в расчете на одного сотрудника = {staff_result}')
else:
    print(f'Финансовый результат - убыль. Убыток составил:{result}')
