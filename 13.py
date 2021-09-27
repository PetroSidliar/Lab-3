def encrypt():
    strings = input('Введіть повідомлення: ')
    even = strings[::2]
    odd = strings[1::2]
    print("Ваше зашифроване повідомлення: ", even + odd)

def decrypt():
    strings = input('Введіть зашифроване повідомлення: ')
    length = len(strings)
    half_length = (length + 1) // 2
    even = strings[:half_length]
    odd = strings[half_length:]
    res = ''
    for i in range(half_length-1):
        join = even[i] + odd[i]
        res += join
    res += even[half_length-1:]
    res += odd[half_length - 1:]
    print("Ваше розшифроване повідомлення: ", res)

decrypt()
encrypt()
