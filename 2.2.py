number = int(input("Enter amount of strings\n"))
s = ''
for i in range(number):
    s1 = input()
    if s1[:2] == '%%':
        s1 = s1[2:]
    if s1[:3] != '###':
        s += s1 + '\n'
print(s)