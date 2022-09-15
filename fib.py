def fib(n):
    if n <= 0:
        print("please input positive number")
        return

    if 0 < n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(1, 10):
    print(fib(i), sep= ' ', end=' ')

