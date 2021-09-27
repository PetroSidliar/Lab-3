def decrypt():
    string=input('Введіть секретне повідомлення: ')
    length=len(string)#для отримання довжини введення 
    half_length=(length+1)//2 #половина вхідних даних 
    even=string[:half_length]#парна частина
    odd=string[half_length:]#непарна частина
#тут ми починаємо вставляти кожну частину, щоб сформувати оригінал
    msg=''
    if length%2==0:
        for i in range (half_length):
            join=even[i]+odd[i]
            msg=msg+join
    else:
        for i in range (1,half_length+1):
            start=i-1
            join=even[start:i]+odd[start:i]
            msg=msg+join
    print(msg)
decrypt()
