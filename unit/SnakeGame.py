import tkinter as tk
import random

# Инициализация окна игры
root = tk.Tk()
root.title("Змейка")

# Параметры игры
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
FPS = 200

# Цвета
WHITE = "#FFFFFF"
GREEN = "#00FF00"
RED = "#FF0000"

# Создание игрового поля
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=WHITE)
canvas.pack()

# Инициализация игровых переменных
snake = [(200, 200)]
snake_direction = "RIGHT"
food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)

# Функция для отрисовки змейки и еды
def draw_snake_and_food():
    canvas.delete("snake", "food")
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + GRID_SIZE, segment[1] + GRID_SIZE, fill=GREEN, tag="snake")
    canvas.create_rectangle(food[0], food[1], food[0] + GRID_SIZE, food[1] + GRID_SIZE, fill=RED, tag="food")

# Функция для движения змейки
def move_snake():
    global snake_direction, food

    head = snake[0]
    if snake_direction == "UP":
        new_head = (head[0], head[1] - GRID_SIZE)
    elif snake_direction == "DOWN":
        new_head = (head[0], head[1] + GRID_SIZE)
    elif snake_direction == "LEFT":
        new_head = (head[0] - GRID_SIZE, head[1])
    elif snake_direction == "RIGHT":
        new_head = (head[0] + GRID_SIZE, head[1])

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        snake.pop()

    draw_snake_and_food()
    root.after(FPS, move_snake)

# Функция для изменения направления змейки
def change_direction(event):
    global snake_direction
    key = event.keysym
    if key == "Up" and snake_direction != "DOWN":
        snake_direction = "UP"
    elif key == "Down" and snake_direction != "UP":
        snake_direction = "DOWN"
    elif key == "Left" and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    elif key == "Right" and snake_direction != "LEFT":
        snake_direction = "RIGHT"

# Начало игры
root.bind("<Key>", change_direction)
move_snake()

root.mainloop()
