import random

class MinesweeperGame:
    def __init__(self, grid_size=5, num_mines=5):
        self.grid_size = grid_size
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.mines = []
        self.generate_mines()
    
    def generate_mines(self):
        for _ in range(self.num_mines):
            mine_row = random.randint(0, self.grid_size - 1)
            mine_col = random.randint(0, self.grid_size - 1)
            while (mine_row, mine_col) in self.mines:  # Ensure mines don't overlap
                mine_row = random.randint(0, self.grid_size - 1)
                mine_col = random.randint(0, self.grid_size - 1)
            self.mines.append((mine_row, mine_col))
    
    def print_board(self, show_mines=False):
        print("   " + " ".join([str(i+1) for i in range(self.grid_size)]))
        print("  " + "+-" * self.grid_size + "+")

        for row in range(self.grid_size):
            print(f"{row+1} | " + " ".join([self.board[row][col] if self.board[row][col] != 'X' or show_mines else ' ' for col in range(self.grid_size)]) + " |")

        print("  " + "+-" * self.grid_size + "+")

    def check_valid_move(self, row, col):
        if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
            print("Invalid move! Out of board bounds.")
            return False
        elif self.board[row][col] != ' ':
            print("You've already uncovered this cell.")
            return False
        else:
            return True
    
    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.grid_size, row + 2)):
            for c in range(max(0, col - 1), min(self.grid_size, col + 2)):
                if (r, c) in self.mines:
                    count += 1
        return count
    
    def uncover_cell(self, row, col):
        if (row, col) in self.mines:
            print("Game over! You hit a mine.")
            self.board[row][col] = 'X'
            self.print_board(show_mines=True)
            return False
        else:
            num_adjacent = self.count_adjacent_mines(row, col)
            self.board[row][col] = str(num_adjacent) if num_adjacent > 0 else ' '
            self.print_board()
            return True
    
    def play_game(self):
        print("Welcome to Minesweeper!")
        print("Uncover all cells without hitting a mine.")

        self.print_board()

        while True:
            try:
                move_row = int(input("Enter row (1-5): ")) - 1
                move_col = int(input("Enter column (1-5): ")) - 1

                if not self.check_valid_move(move_row, move_col):
                    continue
                
                if not self.uncover_cell(move_row, move_col):
                    break

                if all(self.board[row][col] != ' ' for row in range(self.grid_size) for col in range(self.grid_size)):
                    print("Congratulations! You've uncovered all cells without hitting a mine.")
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    game = MinesweeperGame()
    game.play_game()
