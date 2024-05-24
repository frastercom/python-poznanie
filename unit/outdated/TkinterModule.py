import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.title("Мое приложение")
root.geometry("300x200")

# Создание метки (label)
label = tk.Label(root, text="Привет, мир!")
label.pack()

# Создание кнопки
def on_click():
    label.config(text="Кнопка нажата!")

button = tk.Button(root, text="Нажми меня", command=on_click)
button.pack()

# Запуск главного цикла событий
root.mainloop()