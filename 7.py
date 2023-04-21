def fib(n):
    a, b, c = 1, 1, 0
    if n > 2:
        for i in range(n-2):
            c = a + b
            b = a
            a = c
    else:
        print(f"{n}) = 1")
        return
    print(f"{n}) = {c}")

print(fib(int(input("Введите номер номер числа Фиббоначи: "))))
