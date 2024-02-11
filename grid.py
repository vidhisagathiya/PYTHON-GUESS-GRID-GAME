import random

# Function to create the game grid


def create_grid(rows, cols):
    grid = [['X' for _ in range(cols)] for _ in range(rows)]
    return grid

# Function to display the game grid


def display_grid(grid, numbers, revealed=False):
    rows = len(grid)
    cols = len(grid[0])

    # Print column labels
    print("  ", end=" ")
    for col in range(cols):
        print(f"[{chr(col + 65)}]", end=" ")
    print()

    # Print grid cells
    for row in range(rows):
        print(f"[{row+1}]", end=" ")
        for col in range(cols):
            if grid[row][col] == 'X' or (not revealed and grid[row][col] != 'X'):
                print(grid[row][col], end="  ")
            else:
                print(numbers[row * cols + col], end="  ")
        print()

# Function to generate pairs of random numbers


def generate_pairs(rows, cols):
    total_pairs = (rows * cols) // 2
    numbers = [i % total_pairs for i in range(total_pairs)]
    numbers.extend(numbers)  # Duplicate pairs
    random.shuffle(numbers)
    return numbers

# Function to reveal the grid


def reveal_grid(grid, numbers):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            index = row * cols + col
            grid[row][col] = str(numbers[index])

# Function to display the menu and get user's choice


def display_menu():
    print("1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New game")
    print("5. Exit")
    print()
    choice = input("Select: ")
    return choice
