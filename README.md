# Matrix Animation in Terminal

Matrix, just by typing 'm' in your terminal. So you can quickly pull it up for jokes.

## Setup

1. Make sure you have Python installed on your system.

2. Clone this repository or download the `matrix.py` file.

3. Open your `.zshrc` file:

   ```
   nano ~/.zshrc
   ```

4. Add the following code to your `.zshrc`:

   ```zsh
# Function to resize terminal and run matrix.py
run_matrix() {
  # Get screen size
  screen_size=$(stty size)
  rows=$(echo $screen_size | cut -d' ' -f1)
  cols=$(echo $screen_size | cut -d' ' -f2)
  
  # Resize terminal to maximum size (works for iTerm2 and Terminal.app)
  printf '\e[8;'$rows';'$cols't'
  
  # Clear the screen
  clear
  
  # Hide the cursor
  tput civis
  
  # Run the matrix script
  python /Users/markokraemer/Desktop/matrix.py
  
  # Restore cursor
  tput cnorm
  
  # Clear the screen again
  clear
    }

# Alias 'm' to run the matrix function
alias m='run_matrix'
   ```

5. Replace `/path/to/your/matrix.py` with the actual path to your `matrix.py` file.

6. Save and exit the editor (in nano, press Ctrl+X, then Y, and Enter).

7. Apply the changes by running:

   ```
   source ~/.zshrc
   ```

## Usage

After setting up, you can press the 'm' key in your terminal to start the Matrix animation. The terminal will resize to full screen, run the animation, and return to its original state when you exit the script.

To exit the animation, use Ctrl+C.
