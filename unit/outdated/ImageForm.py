import tkinter as tk

window = tk.Tk()
window.title("Image Form")
window.geometry("300x300")

canvas = tk.Canvas(window, width=300, height=300)
img = tk.PhotoImage(file="image.png")
image = canvas.create_image(300, 300, image=img)
canvas.pack()
window.mainloop()