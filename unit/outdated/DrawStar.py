import turtle

def draw_star():
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill()

draw_star()

turtle.mainloop()