import tkinter as tk
window = tk.Tk()
window.title("Калькулятор")
window.geometry("600x600")
text1 = tk.Text(height=1, width=50)
text1.pack()
text2 = tk.Text(height=1, width=50)
text2.pack()
label = tk.Label(text="")
label.pack()

def calculate():
    a = int(text1.get("1.0", "end-1c"))
    b = int(text2.get("1.0", "end-1c"))
    label.config(text=str(a+b))

button = tk.Button(text="Сложить", command=calculate)
button.pack()

window.mainloop()