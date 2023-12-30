strings = list()

while True:
    word = input('Enter word\n')
    if word == 'стоп':
        break
    strings.append(word)

min_word = min(strings, key=len )
max_word = max(strings, key=len)

min_word = set(min_word)
max_word = set(max_word)

if min_word.issubset(max_word):
    print('Yes')
else:
    print('No')

