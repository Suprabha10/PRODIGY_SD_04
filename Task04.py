import tkinter as tk
from tkinter import messagebox

# Sudoku solver using backtracking algorithm
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Tkinter UI
class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # Add instructions
        self.instructions = tk.Label(root, text="Enter numbers in the grid. Press 'Solve Sudoku' to find the solution.")
        self.instructions.grid(row=0, column=0, columnspan=9, padx=5, pady=5)

        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        # Create grid
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(root, width=5, font=("Arial", 16), justify="center", bd=2)
                entry.grid(row=i+1, column=j, padx=2, pady=2)
                entry.bind("<KeyRelease>", self.on_key_release)
                self.entries[i][j] = entry

        # Solve button
        solve_button = tk.Button(root, text="Solve Sudoku", command=self.solve)
        solve_button.grid(row=10, column=0, columnspan=9, pady=10)

    def solve(self):
        self.read_board()
        if solve_sudoku(self.board):
            self.display_board()
        else:
            messagebox.showinfo("Result", "No solution exists!")

    def read_board(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit():
                    self.board[i][j] = int(value)
                else:
                    self.board[i][j] = 0

    def display_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if self.board[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.board[i][j]))

    def on_key_release(self, event):
        # Change color of user inputs
        widget = event.widget
        if widget.get().isdigit():
            widget.config(bg='lightyellow')
        else:
            widget.config(bg='white')

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
