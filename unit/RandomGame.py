import random

a = random.randint(1, 100)
print("Компьютер загадал число от 1 до 100. Попробуйте отгадать")
b = 0
count = 0
while b != a:
    count += 1
    b = int(input("Введите число: "))
    if b > a:
        print("Ваше число больше загаданного")
    elif b < a:
        print("Ваше число меньше загаданного")
print("Вы угадали!")
print("количество попыток: ", count)
