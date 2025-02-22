d = [0] * 100


def fib(n, count_fib):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    count_fib += 1
    d[n] = fib(n - 1, count_fib) + fib(n - 2, count_fib)
    return d[n]


"""
def fibonacci(n):
    count_fibonacci = 0
    f = [0] * 100
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        count_fibonacci += 1
        f[i] = f[i - 1] + f[i - 2]
    return count_fibonacci"""


n = int(input())

count_fib = 0
print(fib(n, count_fib), end=" ")
print(n - 2)
