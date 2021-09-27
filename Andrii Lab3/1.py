f1 = f2 = 1 
n = int(input("Скільки чисел Фібоначчі хочете побачити?\n"))

print(f1, f2, end=' ') 
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
