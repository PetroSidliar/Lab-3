import math


n = int(input("Enter number of months: "))


def savings(n_months):
    return n_months*100 + math.floor(n_months/6)*500 + 300


print(savings(n))
