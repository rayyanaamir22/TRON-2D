# 2D TRON Arcade Game

This is a replica of the 2D Arcade Game TRON via `pygame`. It supports:
- LightCycleBattle with as many LightCycles as you want
- Customizable cycle colours and ribbon lengths

I made this as warmup for the 3D TRON game I wish to make in `Unity` or `OpenGL`. Yep, the game based on the movie based on the game. Stay tuned....

To run:
```
pip install -r requirements.txt
python3 main.py
```

Game Instructions:
There are 2 light cycles (arrow keys, WASD) on the grid, starting at opposite ends. They each emit a finite-length light ribbon, which kills anything that collides with it. Force the opponent to collide with the either light ribbon to win the game.