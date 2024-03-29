"""Возьмем число 192 и умножим его по очереди на 1, 2 и 3:
   192 × 1 = 192
   192 × 2 = 384
   192 × 3 = 576
   Объединяя все три произведения, получим девятизначное число 192384576 из цифр
   от 1 до 9 (пан-цифровое число). Будем называть число 192384576 объединенным произведением
   192 и (1,2,3)
   Таким же образом можно начать с числа 9 и по очереди умножать его на 1, 2, 3, 4 и 5, что в итоге
   дает пан-цифровое число 918273645, являющееся объединенным произведением 9 и (1,2,3,4,5).
   Какое самое большое девятизначное пан-цифровое число можно образовать как объединенное
   произведение целого числа и (1,2, ... , n), где n > 1?"""


def problem_38():
    "Функция решения задачи проекта Эейлера №38"
    list_num = []
    for i in range(1, int(10000) + 1):
        current_num = ''
        for j in range(1, 10):
            if len(current_num) < 9:
                current_num += str(i * j)
            else:
                break
        list_num.append(current_num)

    return max(i for i in list_num if len(i) == 9)


if __name__ == '__main__':
    print(problem_38())
