# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

profit = float(input("Введите выручку фирмы "))
charge = float(input("Введите издержки фирмы "))
if profit > charge:
    print(f"Фирма работает с прибылью. Рентабельность составляет: {(profit - charge) / profit * 100: .1f} %")
    # рентабельность фирмы = прибыль / выручку * 100%
    staffs = int(input("Введите количество сотрудников фирмы: "))
    print(f'Чистая прибыль на одного сотрудника составялет: {(profit - charge) / staffs: .2f} $')
elif profit == charge:
    print("Фирма работает в ноль.")
else:
    print("Фирма работает в убыток.")
