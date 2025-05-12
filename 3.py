def square_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield b * b
        a, b = b, a + b

print(*square_fibonacci(5))