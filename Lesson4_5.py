# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_items = [el for el in range(99, 1001) if el % 2 == 0]
print(my_items)
all_multiply = reduce(lambda a,b: a * b, my_items)
print(all_multiply)