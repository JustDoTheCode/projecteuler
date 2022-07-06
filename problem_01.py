"""Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
   Сумма этих чисел равна 23.
   Найдите сумму всех чисел меньше 1000, кратных 3 или 5."""


def problem_1():
    "Функция решения задачи проекта Эейлера №1"

    return sum((i for i in range(0, 1000) if (i % 3 == 0 or i % 5 == 0)))


if __name__ == '__main__':
    print(problem_1())
