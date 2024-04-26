a = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]
min = a[0]
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
print(min)