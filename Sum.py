# Сумма цифр (555=5+5+5=15)

num = int(input("Введите целое: ")) # Запрашиваем ввод числа
sum = 0 # Объявляем переменную
while (num != 0): # В цикле (while) происходит суммирование цифр
    sum = sum + num % 10 # Полученный младший разряд прибавляется к переменной сумме
    num = num // 10 # Используем целочисленное деление
print("Сумма цифр числа равна: ", sum) # Выводим результат суммирование в консоль