def fibonacci(N):
    if N == 0:
        return 0

    elif N == 1:
        return 1

    return fibonacci(N - 1) + fibonacci(N - 2)


N = 7
for i in range(N + 1):
    print(f"{i} Fibonacci term is: ", fibonacci(i))

