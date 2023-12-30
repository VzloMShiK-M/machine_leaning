def greet():
    first_name = input('Введите ваше имя:\n')
    second_name = input('Введите вашу фамилию:\n')

    print('Здравствуйте, ', end= '')
    print(first_name, end= ' ')
    print(second_name, end= '')

greet()