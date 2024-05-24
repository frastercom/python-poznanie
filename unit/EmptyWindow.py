import tkinter as tk
window = tk.Tk()
window.title("Моя первая программа")
window.geometry("600x600")
label = tk.Label(window, text="Привет, мир!")
label.pack()

def on_click():
    i =+ 1
    l = tk.Label(window, text=str(i))
    l.pack()

button = tk.Button(window, text="Кнопка", command = on_click)
button.pack()

text = tk.Text(window)
text.pack()

def on_clickClear():
    t = text.get("1.0", tk.END)
    text.delete("1.0", tk.END)
    text.insert("1.0", t.replace(" ", ""))

button1 = tk.Button(window, text="Удалить пробелы",
                    command = on_clickClear)
button1.pack()

window.mainloop()