def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

n = int(input('Enter a number to tell how precise the calculation has to be :'))


def calc(n):
    e = 0
    for i in range(1, n+1):
        e += 1/factorial(n)
    return e

print(calc(n))
