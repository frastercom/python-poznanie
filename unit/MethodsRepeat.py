def sum_array(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i] # sum = sum + array[i]
    return sum

def multyplay_array(array):
    mul = 0
    for i in range(len(array)):
        mul *= array[i]  # mul = mul * array[i]
    return mul

a = []
for i in range(5):
    a.append(int(input("введите число")))
print(sum_array(a))
print(multyplay_array(a))