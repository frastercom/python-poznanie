import turtle


def move_to_click(x, y):
    turtle.goto(x, y)


turtle.onscreenclick(move_to_click)

turtle.mainloop()
