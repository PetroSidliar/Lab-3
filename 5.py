a = int(input("Введіть ціле число: "))
b = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        b = b+1
if (b <= 0):
    print("Число просте")
else:
    print("Число не є простим")
