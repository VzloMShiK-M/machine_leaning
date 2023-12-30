number_of_strings = int(input('Введите количество строк:\n'))
# strings = list()

FLAG = 0
for i in range(number_of_strings):
    string = (input('Введите слово\n'))
    if string.find('кот') != -1:
        FLAG = 1

    elif string.find('Кот') != -1:
        FLAG = 1

# print(strings)
if FLAG == 1:
    print('МЯУ')
else:
    print('НЕТ')