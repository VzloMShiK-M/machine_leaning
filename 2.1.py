number = int(input("Enter amount of numbers\n"))
array = []
print('Enter numbers')
for i in range(number):
    array.append(int(input()))

array = array[::-1]
print(array)