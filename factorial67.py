def factorial(n):
    """
    Вычисляет факториал числа n рекурсивно с проверкой входных данных.

    Args:
        n: неотрицательное целое число

    Returns:
        n! (произведение всех чисел от 1 до n)

    Raises:
        TypeError: если n не является целым числом
        ValueError: если n отрицательное
    """
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Тесты
if __name__ == "__main__":
    test_cases = [0, 1, 5, 10]
    for test in test_cases:
        print(f"{test}! = {factorial(test)}")

    # Проверка ошибок
    try:
        factorial(-5)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        factorial(3.14)
    except TypeError as e:
        print(f"Ошибка: {e}")