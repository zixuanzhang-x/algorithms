def factorial(n: int) -> int:
    if n < 0:
        raise RuntimeError

    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(0))
print(factorial(5))