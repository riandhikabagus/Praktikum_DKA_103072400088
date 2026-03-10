def Fibonacci(n):
    x = 0
    y = 1
    for i in range(n-1):
        x, y = y, x + y
    return x


def cetakFibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x, end=" ")
        x, y = y, x + y


n = int(input("Masukkan n: "))

print("Fibonacci ke-", n, "=", Fibonacci(n))
cetakFibonacci(n)