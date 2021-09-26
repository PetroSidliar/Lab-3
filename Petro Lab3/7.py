print('Enter a text and when finished press Enter twice: ')
text = ''

while True:
    line = input()
    if line:
        text += line + '\n '
    else:
        break


def wc(text):
    n_words = len(text.split(' ')) - 1
    n_lines = len(text.split('\n')) - 1
    n_characters = len(text) - 2*n_lines
    print(f'Characters in text - {n_characters}')
    print(f'Words in text - {n_words}')
    print(f'Lines in text - {n_lines}')


wc(text)
      

