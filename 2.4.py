def Artek(s, max_number):
    s = s.split(',')
    artek = []
    for i in s:
        if i[-1] == '5':
            artek.append(i[:-2])
    artek = sorted(artek)
    if len(artek) > max_number:
        return ','.join(artek[:max_number])
    else:
        return ','.join(artek)


s = input('Enter list of students:\n')
max_number = int(input('Enter max number of seats:\n'))

print('List of trip participant', Artek(s, max_number))
