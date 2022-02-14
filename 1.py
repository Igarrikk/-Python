# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

name = 'Игорь'
age = 43
print(name, age)

name = input('Введите имя: ')
age = int(input('Сколько вам лет?: '))
period = 50
age_period = age + period
stroka = 'Привет, ' + name + ', через ' + str(period) + ' лет Вам будет ' + str(age_period)  # 1 метод
print(stroka)
stroka = 'Привет, {}, через {} лет Вам будет {} ' .format(name, period, age_period)  # 2 метод
print(stroka)

