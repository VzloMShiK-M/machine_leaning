number = int(input("Enter amount of numbers\n"))
s = []
print('Enter numbers\n')
for i in range(number):
    s.append(int(input()))

n1 = int(input('Enter left index\n'))
n2 = int(input('Enter right index\n'))

j = 0
sum_of_numbers = 0
for i in s:
    if (j >= n1) and (j <= n2):
        sum_of_numbers += i
    j += 1
print(sum_of_numbers)