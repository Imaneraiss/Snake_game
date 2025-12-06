import tkinter as tk
import random
import winsound

# game window
ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tk.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tk.Canvas(window, bg="black", height=WINDOW_HEIGHT, width=WINDOW_WIDTH, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

# center window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# initialize game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
snake_body = []
velocityX = 0
velocityY = 0
game_over = False
score = 0

def detected_diretion(e):
    global velocityX, velocityY, game_over

    if e.keysym == "r" or e.keysym == "R":
        restart_game()
        return
    
    if game_over:
        return
    
    if e.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score
    if game_over:
        return
    
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        play_game_over_sound()
        return
        
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            play_game_over_sound()
            return
            
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1
        play_eat_sound()

    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, food, snake_body, game_over, score
    move()
    canvas.delete("all")
    
    canvas.create_rectangle(food.x, food.y, food.x+TILE_SIZE, food.y+TILE_SIZE, fill="yellow")
    canvas.create_rectangle(snake.x, snake.y, snake.x+TILE_SIZE, snake.y+TILE_SIZE, fill="pink")

    for tiles in snake_body:
        canvas.create_rectangle(tiles.x, tiles.y, tiles.x+TILE_SIZE, tiles.y+TILE_SIZE, fill="pink")

    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="Arial 20", text=f"Game Over: {score}", fill="white")
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2+30, font="Arial 12", text="Press R to Restart", fill="white")
    else:
        canvas.create_text(30, 20, font="Arial 10", text=f"Score: {score}", fill="white")

    window.after(200, draw)

def restart_game():
    global snake, food, snake_body, velocityX, velocityY, game_over, score
    snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)
    food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
    snake_body = []
    velocityX = 0
    velocityY = 0
    game_over = False
    score = 0
def play_eat_sound():
    winsound.Beep(1000, 100)  # High pitch beep

def play_game_over_sound():
    winsound.Beep(400, 300)  # Low pitch beep

draw()
window.bind("<KeyRelease>", detected_diretion)
window.mainloop()