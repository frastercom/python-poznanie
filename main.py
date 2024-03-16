import turtle
def draw_star():
    turtle.bgcolor("black")
    n = int(input("введите количество углов"))
    sise =int(input("введите розмер звезды"))


    turtle.begin_fill()
    r = int(720/n)
    for _ in range(5):
        turtle.forward(sise)
        turtle.right(r)
    turtle.end_fill()



    #turtle.onscreenclick(draw_rectangle)
draw_star()
turtle.mainloop()

