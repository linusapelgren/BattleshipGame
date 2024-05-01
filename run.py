import random
import time


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['O' for _ in range(size)] for _ in range(size)]
        self.ship_locations = []
        time.sleep(0.5)
        for _ in range(size):
            while True:
                ship_location = [random.randint(0, size-1) for _ in range(2)]
                if ship_location not in self.ship_locations:
                    self.ship_locations.append(ship_location)
                    self.board[ship_location[0]][ship_location[1]] = 'S'
                    break

    def print_computer_board(self):
        for row_idx, row in enumerate(self.board, start=1):
            printable_row = []
            for col_idx, cell in enumerate(row, start=1):
                if cell == '*' or cell == 'X':
                    printable_row.append(cell)
                elif self.board[row_idx - 1][col_idx - 1] == 'S':
                    printable_row.append('O')
                else:
                    printable_row.append('O')
            print(" ".join(printable_row))

    def print_player_board(self):
        for row_idx, row in enumerate(self.board, start=1):
            printable_row = []
            for col_idx, cell in enumerate(row, start=1):
                if cell == '*' or cell == 'X':
                    printable_row.append(cell)
                else:
                    printable_row.append(cell)
            print(" ".join(printable_row))

    def guess(self, row, col):
        if [row, col] in self.ship_locations:
            self.board[row][col] = 'X'
            print("Ship sunk!")
            self.ship_locations.remove([row, col])
            return len(self.ship_locations) == 0
        elif self.board[row][col] == 'X' or self.board[row][col] == '*':
            print("Already guessed!")
            return False
        else:
            self.board[row][col] = '*'
            print("Missed!")
            return False


def play_game():
    print("Choose board size:")
    print("1. 5x5")
    print("2. 10x10")
    print("3. 15x15")
    while True:
        try:
            size = int(input("Enter 1, 2, or 3:\n"))
            if size == 1:
                size = 5
                break
            elif size == 2:
                size = 10
                break
            elif size == 3:
                size = 15
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid choice! Please enter a number.")
    player_board = Board(size)
    computer_board = Board(size)
    while True:
        time.sleep(0.5)
        print("Player's turn")
        time.sleep(0.5)
        print("Player board:")
        time.sleep(0.5)
        player_board.print_player_board()
        time.sleep(0.5)
        print("Computer board:")
        time.sleep(0.5)
        computer_board.print_computer_board()
        time.sleep(0.5)
        while True:
            try:
                guess_row = int(input("Guess Row:"))
                guess_col = int(input("Guess Col:"))
                if guess_row < 0 or guess_row >= size:
                    print("Invalid guess! Enter number between 0 and", size-1)
                    continue
                if guess_col < 0 or guess_col >= size:
                    print("Invalid guess! Enter number between 0 and", size-1)
                    continue
                else:
                    break
            except ValueError:
                print("Invalid guess! Please enter a number.")

        if computer_board.guess(guess_row, guess_col):
            print("Player wins!")
            break

        time.sleep(0.5)
        print("Computer's turn")
        guess_row = random.randint(0, size-1)
        guess_col = random.randint(0, size-1)
        time.sleep(0.5)
        print("Computer guessed Row:", guess_row)
        time.sleep(0.5)
        print("Computer guessed Col:", guess_col)

        if player_board.guess(guess_row, guess_col):
            print("Computer wins!")
            break


while True:
    play_game()
    play_again = input("Play again? (Y/N): \n")
    if play_again.lower() != 'y':
        break
