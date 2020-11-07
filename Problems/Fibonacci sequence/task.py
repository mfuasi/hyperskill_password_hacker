def fibonacci(n):
    f0, f1 = 0, 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1


