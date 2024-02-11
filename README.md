# Memory Testing Game

This is a Python console-based memory testing game where players uncover hidden pairs of numbers on a grid. The game features a simple menu interface, error checking, and scoring system.

## Overview

The game allows players to interact with a grid of hidden numbers, aiming to uncover pairs in as few guesses as possible. Key features include:

- Supports grid sizes of 2x2, 4x4, and 6x6.
- Object-oriented implementation with `grid.py` managing game logic and `game.py` handling user interface.
- Error checking ensures valid inputs from the player.
- Scoring system calculates player's efficiency based on guess count.

## How to Play

1. Run `game.py` from the command line, specifying the grid size (2, 4, or 6). [Command : python3 game.py 4]
2. Follow the on-screen prompts to select menu options and input cell coordinates.
3. Uncover pairs of numbers on the grid using Menu Option 1 or manually reveal cells using Menu Option 2.
4. Aim to uncover all pairs in the grid with the fewest guesses possible to achieve a higher score.

## File Structure

- `game.py`: Contains the user interface code, including menu, prompts, and score display.
- `grid.py`: Manages the grid structure, hidden number pairs, and game logic.

