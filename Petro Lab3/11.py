num = input('Enter a large integer: ')

res = ''
count= 0

for i in num[::-1]:
    count += 1
    res += i
    if count % 3 == 0:
        res += ','


if len(num)%3 == 0:
    print(res)
    print(res[-2::-1])
else:
    print(res[::-1])

