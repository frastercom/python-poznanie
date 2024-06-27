import tkinter as tk
import random

# Список персонажей
characters = [

    {"name": "Дональд Дак", "image": "donald_duck.gif"}
]

# Инициализация окна игры
root = tk.Tk()
root.title("Угадай персонажа")

# Создание игрового поля
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Функция для отображения случайного персонажа
def display_character():
    global current_character, current_image
    current_character = random.choice(characters)
    current_image = tk.PhotoImage(file=current_character["image"])
    canvas.create_image(200, 200, image=current_image)
    canvas.create_text(200, 350, text=f"Угадай персонажа: {current_character['name']}", font=("Arial", 16))

# Функция для проверки ответа
def check_answer(event):
    if event.char.lower() == current_character["name"].lower():
        canvas.delete("all")
        canvas.create_text(200, 200, text="Правильно!", font=("Arial", 24))
        canvas.after(2000, display_character)
    else:
        canvas.create_text(200, 300, text="Неправильно, попробуй еще раз!", font=("Arial", 16))

# Начало игры
display_character()
root.bind("<Key>", check_answer)
root.mainloop()
