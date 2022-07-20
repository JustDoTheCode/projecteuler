"""Последовательность Фибоначчи определяется рекурсивным правилом:
   Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
   Таким образом, первые 12 членов последовательности равны:
   F1 = 1
   F2 = 1
   F3 = 2
   F4 = 3
   F5 = 5
   F6 = 8
   F7 = 13
   F8 = 21
   F9 = 34
   F10 = 55
   F11 = 89
   F12 = 144
   Двенадцатый член F12 - первый член последовательности, который содержит три цифры.
   Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?"""


def problem_25():
    "Функция решения задачи проекта Эейлера №25"

    memo = {1: 1, 2: 1}

    def fibonacci_with_memo(n):
        return memo[n - 1] + memo[n - 2]

    n = 3

    while True:
        current_result = fibonacci_with_memo(n)
        memo[n] = current_result
        if len(str(current_result)) == 1000:
            return n
        n += 1


if __name__ == '__main__':
    print(problem_25())