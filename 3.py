# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

namber = input('Введите число: ')
otvet = int(namber) + int(namber + namber) + int(namber + namber + namber)
print(otvet)
