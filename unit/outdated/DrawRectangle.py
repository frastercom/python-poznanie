import turtle


def draw_rectangle(x, y):
    width = int(input("Введите ширину прямоугольника: "))
    height = int(input("Введите высоту прямоугольника: "))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


turtle.onscreenclick(draw_rectangle)

turtle.mainloop()
