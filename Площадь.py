# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.

from math import pi
R = float(input())
S = pi * R ** 2
C = 2 * pi * R
print(S)
print(C)
