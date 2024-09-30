import random
import time
import os

# Get terminal width and height
width, height = os.get_terminal_size()

# Matrix characters
matrix_chars = ['0', '1']

# ANSI escape code for green text
green_code = '\033[32m'

# ANSI escape code to reset text color
reset_code = '\033[0m'

# Generate random screen
screen = [[random.choice(matrix_chars) for _ in range(width)] for _ in range(height)]

while True:
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print the screen with green text
    for row in screen:
        print(f'{green_code}{" ".join(row)}{reset_code}')
        
    # Update screen by shifting rows down
    for i in reversed(range(1, height)):
        screen[i] = screen[i-1]
    
    # Generate new top row
    screen[0] = [random.choice(matrix_chars) for _ in range(width)]
    
    # Wait for a short duration to simulate animation
    time.sleep(0.1)
