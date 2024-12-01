from math import sqrt


def is_prime(func):
    def wrapper(*args):
        result = func(*args)

        # Проверка на простоту числа
        if result <= 1:
            print("Не простое")
        else:
            for i in range(2, int(sqrt(result)) + 1):
                if result % i == 0:
                    print("Составное")
                    return result
            print("Простое")

        return result

    return wrapper


# Функция для сложения трех чисел
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Вызываем функцию
result = sum_three(2, 3, 6)
print(result)
