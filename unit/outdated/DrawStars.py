import turtle

def draw_star(x, y, size, vertices):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.begin_fill()

    for i in range(vertices):

        turtle.forward(size)
        angle = vertices // 2 * 360 / vertices
        turtle.left(angle)

    turtle.end_fill()

def handle_click(x, y):
    size = int(input("Введите размер звезды: "))
    vertices = int(input("Введите количество вершин звезды: "))
    #size=30
    #vertices=5
    draw_star(x, y, size, vertices)

turtle.onscreenclick(handle_click)

turtle.mainloop()