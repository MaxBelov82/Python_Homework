

list_number = []
for i in range(4):
    list_number.append (int(input('Введите числа -'))) 
max_number = list_number[0]
for i in range(4):
    if max_number < list_number[i]:
        max_number = list_number[i]
print(max_number)
