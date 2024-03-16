import turtle
import random

def move_to_click(x, y):
   new_x= random.randint(-200, 200)
   new_y = random.randint(-200, 200)
   turtle.goto(new_x,new_y)

turtle.onscreenclick(move_to_click)
turtle.shape("turtle")
turtle.mainloop()
