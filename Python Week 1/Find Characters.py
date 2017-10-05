x = ['hello','world','my','name','is','Anna']
y = 'o'
new_list = []

for val in range(0, len(x)):
    if (x[val].find(y)) != -1:
        new_list.append(x[val])
print(new_list)
