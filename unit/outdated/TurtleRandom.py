import turtle
import random


def move_to_random(x, y):
    new_x = random.randint(-200, 200)
    new_y = random.randint(-200, 200)
    turtle.goto(new_x, new_y)


turtle.shape("turtle")
turtle.onscreenclick(move_to_random)

turtle.mainloop()
