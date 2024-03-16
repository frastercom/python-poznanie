import turtle
import random

def draw_star(x, y, size, vertices):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color("yellow")
    turtle.begin_fill()

    for _ in range(vertices):
        if vertices%2!=0:
            turtle.forward(size)
            angle =  vertices // 2 * 360 / vertices
            turtle.right(angle)

    turtle.end_fill()

def handle_click(x, y):
    size = random.randint(20, 100)
    vertices = random.randint(5, 10)
    turtle.bgcolor("black")
    draw_star(x, y, size, vertices)

turtle.onscreenclick(handle_click)

turtle.mainloop()