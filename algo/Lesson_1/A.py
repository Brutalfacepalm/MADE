# Заданы два целых числа a и b. Выведите a+b.
#
# Входные данные
# В первой строке записано целое число t (1≤t≤104) — количество наборов входных данных в тесте.
# Далее следуют t наборов входных данных.
#
# Каждый набор задан одной строкой, которая содержит два целых числа a, b (−1000≤a,b≤1000).
#
# Выходные данные
# Выведите t целых чисел — искомые суммы a+b для каждого набора входных данных.


for _ in range(int(input())):
    s = sum(map(int, input().split()))
    print(s)