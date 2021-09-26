s = input('Enter a string: ')

unique = []

for i in s:
    if i not in unique:
        unique.append(i)

print(f'Number of distinct characters in a string is {len(unique)}')

