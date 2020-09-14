# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем 
# смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:

# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести
# название вторичного цвета, который получится в результате.

x, y = str(input()), str(input())
if x == 'красный' and y == 'синий':
    print('фиолетовый')
elif x == 'синий' and y == 'красный':
    print('фиолетовый')
elif x == 'красный' and y == 'желтый':
    print('оранжевый')
elif x == 'желтый' and y == 'красный':
    print('оранжевый')
elif x == 'синий' and y == 'желтый':
    print('зеленый')
elif x == 'желтый' and y == 'синий':
    print('зеленый')
elif x =='красный' and y =='красный':
    print('красный')
elif x =='синий' and y =='синий':
    print('синий')
elif x =='желтый' and y =='желтый':
    print('желтый')
else:
    print('ошибка цвета')
