import time
import sys
import os
from grid import create_grid, display_grid, generate_pairs, reveal_grid, display_menu

# Main game loop


def play_game(rows, cols):
    total_pairs = rows * cols // 2  # Calculate total pairs based on grid size

    grid = create_grid(rows, cols)
    numbers = generate_pairs(rows, cols)
    revealed_grid = False
    score = 0
    guessed_pairs = 0
    guesses = 0
    guesses2 = 0

    while True:
        print("--------------------")
        print("|    PEEK-A-BOO    |")
        print("--------------------")

        if revealed_grid:
            # Display the grid with revealed numbers
            display_grid(grid, numbers)
        else:
            # Display the game grid with hidden numbers
            display_grid(grid, ['X'] * len(numbers))

        print()

        choice = display_menu()
        if choice not in ['1', '2', '3', '4', '5']:
            os.system('clear')
            print("Invalid choice! Please enter a number between 1 and 5.")
            print()
            continue

        if choice == '1':
            if revealed_grid:
                os.system('clear')
                print("Cannot guess a cell when the grid is revealed!")
                print()
                continue

            valid_coordinates = False
            while not valid_coordinates:
                cell1 = input("Enter cell coordinates (e.g., A1): ")
                cell2 = input("Enter cell coordinates (e.g., B2): ")

                # Verify if the entered coordinates are valid
                if len(cell1) != 2 or len(cell2) != 2:
                    print("Invalid cell coordinates! Please enter valid coordinates.")
                    print()
                    continue

                row1 = int(cell1[1]) - 1
                col1 = ord(cell1[0].upper()) - 65
                row2 = int(cell2[1]) - 1
                col2 = ord(cell2[0].upper()) - 65

                # Check if the entered coordinates are within the grid bounds
                if not (0 <= row1 < rows and 0 <= col1 < cols) or not (0 <= row2 < rows and 0 <= col2 < cols):
                    print("Invalid cell coordinates! Please enter valid coordinates.")
                    print()
                    continue

                # Check if the same cell is selected twice
                if (row1, col1) == (row2, col2):
                    print(
                        "Cannot select the same cell twice! Please enter different coordinates.")
                    print()
                    continue

                valid_coordinates = True

            if grid[row1][col1] == 'X' or grid[row2][col2] == 'X':
                grid[row1][col1] = str(numbers[row1 * cols + col1])
                grid[row2][col2] = str(numbers[row2 * cols + col2])
                print("Numbers Revealed")
                display_grid(grid, numbers)
                time.sleep(2)
                
                os.system('clear')

                if grid[row1][col1] != grid[row2][col2]:
                    guesses += 1
                    grid[row1][col1] = 'X'
                    grid[row2][col2] = 'X'
                else:
                    guessed_pairs += 1
                    guesses += 1
                    grid[row1][col1] = str(numbers[row1 * cols + col1])
                    grid[row2][col2] = str(numbers[row2 * cols + col2])
                    if (guessed_pairs == total_pairs):
                        score = 100 * (total_pairs / guesses)
                        print("Congratulations! You have won!! Your score is:", round(score, 2))

            else:
                os.system('clear')
                print("Cell already revealed!")

        elif choice == '2':
            if revealed_grid:
                os.system('clear')
                print("Cannot manually reveal a cell when the grid is revealed!")
                print()
                continue

            valid_coordinates = False
            while not valid_coordinates:
                cell = input(
                    "Enter the cell coordinates to reveal (e.g., A1): ")

                # Verify if the entered coordinates are valid
                if len(cell) != 2:
                    print("Invalid cell coordinates! Please enter valid coordinates.")
                    print()
                    continue

                row = int(cell[1]) - 1
                col = ord(cell[0].upper()) - 65

                # Check if the entered coordinates are within the grid bounds
                if not (0 <= row < rows and 0 <= col < cols):
                    print("Invalid cell coordinates! Please enter valid coordinates.")
                    print()
                    continue

                valid_coordinates = True

            if grid[row][col] == 'X':
                grid[row][col] = str(numbers[row * cols + col])

                print("Cell revealed!")
                os.system('clear')
                guesses += 2
                guesses2 += 1

                if guesses2 >= total_pairs * 2 and guessed_pairs == 0:
                    revealed_grid = True
                    os.system('clear')
                    print("You cheated - Loser! Your score is 0!")

            else:
                os.system('clear')
                print("Cell already revealed!")


        elif choice == '3':
            os.system('clear')
            if revealed_grid:
                os.system('clear')
                print("Grid already revealed.")
                print()
                continue

            revealed_grid = True
            os.system('clear')
            reveal_grid(grid, numbers)

        elif choice == '4':
            os.system('clear')
            grid = create_grid(rows, cols)
            numbers = generate_pairs(rows, cols)
            revealed_grid = False
            score = 0
            guessed_pairs = 0
            guesses = 0
            guesses2 = 0

        elif choice == '5':
            sys.exit()

        print()


# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python game.py <grid_size>")
    print("Valid grid sizes: 2, 4, 6")
    sys.exit()

# Get the grid size from command line argument
grid_size = int(sys.argv[1])

# Check if the grid size is valid
if grid_size not in [2, 4, 6]:
    print("Invalid grid size! Exiting the game.")
else:
    # Start the game
    while True:
        play_game(grid_size, grid_size)
