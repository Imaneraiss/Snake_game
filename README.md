# 🐍 Snake Game in Python

A classic Snake game built with Python's Tkinter library, featuring sound effects and smooth gameplay.


##  Features

- **Classic Snake Gameplay**: Control the snake to eat food and grow longer
- **Score Tracking**: Keep track of your current score
- **Sound Effects**: Audio feedback when eating food or game over
- **Collision Detection**: Game ends when hitting walls or yourself
- **Restart Function**: Press 'R' to restart after game over
- **Centered Window**: Game window automatically centers on screen

## 🎮 How to Play

- **Arrow Keys**: Control snake direction (Up, Down, Left, Right)
- **R Key**: Restart the game after game over
- **Objective**: Eat the yellow food to grow and increase your score
- **Avoid**: Hitting walls or your own body

## 🛠️ Technologies Used

- **Python 3.13**
- **Tkinter** - GUI framework
- **Winsound** - Sound effects (Windows only)
- **Random** - Food placement

## 📋 Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- Windows OS (for sound effects)

##  Installation & Running

1. **Clone the repository**
```bash
git clone https://github.com/Imaneraiss/Snake_game.git
cd Snake_game
```

2. **Run the game**
```bash
python snake.py
```

##  Game Rules

- The snake moves continuously in the current direction
- Eating food (yellow square) increases score by 1 and grows the snake
- Game ends if the snake hits the wall or itself
- Final score is displayed on game over screen

## Customization

You can modify these constants in the code:
- `ROWS` and `COLS`: Change grid size (default: 25x25)
- `TILE_SIZE`: Change size of each tile (default: 25 pixels)
- `window.after(200, draw)`: Change game speed (lower = faster)

## Future Improvements

- [ ] High score tracking and persistence
- [ ] Difficulty levels (Easy, Medium, Hard)
- [ ] Pause functionality
- [ ] Start menu screen
- [ ] Cross-platform sound support

##  Author

**Imane Raiss**
- GitHub: [@Imaneraiss](https://github.com/Imaneraiss)

## 📄 License

This project is open source and available for educational purposes.

---
*Developed as a learning project to demonstrate Python programming skills*