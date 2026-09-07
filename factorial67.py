def factorial(n):
    """
    Вычисляет факториал числа n рекурсивно.

    Args:
        n: неотрицательное целое число

    Returns:
        n! (произведение всех чисел от 1 до n)
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Примеры использования
if name == "main":
    print(f"5! = {factorial(5)}")  # 120
    print(f"0! = {factorial(0)}")  # 1
    print(f"1! = {factorial(1)}")  # 1