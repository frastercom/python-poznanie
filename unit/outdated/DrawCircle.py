import turtle


def draw_circle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)


turtle.onscreenclick(draw_circle)

turtle.mainloop()
