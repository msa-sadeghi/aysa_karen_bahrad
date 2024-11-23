from tkinter import *
from random import randint


class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        for i in range(BODY_SIZE):
            self.coordinates.append([0,0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="yellow", tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self) -> None:
        x = randint(0, GAME_WIDTH // SPACE_SIZE) * SPACE_SIZE
        y = randint(0, GAME_HEIGHT // SPACE_SIZE) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="red", tag="food")


def next_turn(snake, food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, [x,y])
    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="yellow", tag="snake")
    snake.squares.insert(0, square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        score_label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    



BODY_SIZE = 2
SPACE_SIZE = 50
GAME_WIDTH = 700
GAME_HEIGHT = 700
direction = "down"
score = 0
window = Tk()
window.title("Snake")
window.resizable(False, False)

score_label = Label(window, text=f"Score: {score}", font=("arial", 22))
score_label.pack()
canvas = Canvas(window, bg="black", width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()


window.update()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()

x = screen_width//2 - window_width//2
y = screen_height//2 - window_height//2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()
next_turn(snake, food)
window.mainloop()