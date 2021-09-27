def encrypt():
    strings=input('Введіть повідомлення: ')
    even=strings[::2]
    odd=strings[1::2]
    print(even+odd)
encrypt() 
