def factorial(number : int) -> int:
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result
    