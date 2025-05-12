def factorials(n):
    factor = 1
    for i in range(1, n + 1):
        factor *= i
        yield factor


print(*factorials(5))
