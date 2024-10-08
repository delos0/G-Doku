# G-Doku

## Overview
This project is a grid-based puzzle solver written in Python. It allows users to input the size of the grid and a numeric constraint, then interact with the grid by making moves. The program validates the board and checks if the puzzle is solved according to the rules provided.

## Features
- **Dynamic Board Creation**: Create a grid of size `k x k`, where `k` is provided by the user.
- **Move Handling**: Users can input values into the grid, and the program automatically places them in specific cells based on the game's rules.
- **Board Validation**: After each move, the board is checked to ensure the values adhere to predefined constraints.
- **Puzzle Solving**: The program tracks if the board is correctly solved by ensuring that no invalid moves are made.

## How It Works
1. **Input**: The program prompts for two inputs:
   - `k`: Defines the size of the board (`k x k`).
   - `n`: The numeric constraint that the sum of values in certain regions of the board must not exceed.
   
2. **Board Display**: The grid is printed to the console after every move. Empty cells are represented by blank spaces, and the board adjusts dynamically based on user input.

3. **Making Moves**: Players enter moves that are placed in specific cells of the grid. The program handles the board’s layout, ensuring values are placed according to the game’s logic.

4. **Validation**: The board is validated by checking the sum of values in designated regions. If the sum exceeds the constraint `n`, the board is deemed invalid.

## How to Use
1. Clone or download the project.
2. Ensure you have Python installed on your system.
3. Run the script:
   ```bash
   python Main.py
4. Follow the prompts to input the grid size (k) and the constraint (n).
5. Make moves to fill the grid and try to solve the puzzle. Please use the example input file to format your input.
