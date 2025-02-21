from module import *

class Game:
    def __init__(self, names: list[str], board_size: int) -> None:
        self.names: dict[str, str] = {'X': names[0], 'O': names[1]}
        self.scores: dict[str, int] = {'X': 0, 'O': 0}

        self.board: list[list[str]] = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.board_size: int = board_size
        self.board_map: dict[str, int] = {chr(65 + i): i for i in range(board_size)}
        self.win_count= min(5, board_size)
        
    def reset_board(self) -> None:
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def draw_board(self) -> None:
        number_coordinates_row: str = f'   {'   '.join(str(i+1) for i in range(self.board_size))}'
        rows: list[str] = [f"{chr(65 + i)}  {' | '.join(row)}" for i, row in enumerate(self.board)]
        rows_separator: str = f'\n  {'+'.join('---' for _ in range(self.board_size))}\n'

        print(number_coordinates_row)
        print(rows_separator.join(rows))

    def write(self, target: str, position: str) -> bool:
        if not self.valid(position):
            return False
        
        i: int = self.board_map[position[0].upper()]
        j: int = int(position[1]) - 1

        if self.is_empty(i,j):
            self.board[i][j] = target
            return True

    def choose(self, target: str) -> None:
        position = input(f'\n{self.names[target]}, choose your position: ')
        while not self.write(target, position):
            position = input()

    def valid(self, position: str) -> bool:
        # string len must be 2
        if len(position) != 2:
            clear_line()
            print_inline(f'Position error: {position} is not a valid position format.\nPlease try again: ')
            return False
        
        # string must be [letter, number]
        if not (position[0].isalpha() and position[1].isdigit()):
            clear_line()
            print_inline(f'Position error: {f'{position[0]} is not a letter' if not position[0].isalpha() else f'{position[1]} is not an integer'}\nPlease try again: ')
            return False
        
        # catch board_map key error
        if not position[0].upper() in self.board_map:
            key1 = next((key for key, value in self.board_map.items() if value == 0), None)
            key2 = next((key for key, value in self.board_map.items() if value == self.board_size-1), None)
            clear_line()
            print_inline(f'Position error: {position[0].upper()} is out of range. (must be between {key1} and {key2}).\nPlease try again: ')
            return False
        
        # number must not be greater than size
        if int(position[1]) > self.board_size or int(position[1]) <= 0:
            clear_line()
            print_inline (f'Position error: {position[1]} is out of range. (must be between 1 and {self.board_size}).\nPlease try again: ')
            return False
        
        return True
    
    def is_empty(self,i: int, j: int) -> bool:
        if self.board[i][j] == ' ':
            return True
        
        clear_line()
        print_inline('This position is already taken. Please try again: ')
        return False

    def refresh(self, target: str) -> None:
        clear_terminal()
        self.draw_board()
        self.choose(target)

    def win(self, target: str) -> None:
        for row in self.board:
            if row.count(target) == self.win_count:
                return True
        for col in zip(*self.board):
            if col.count(target) == self.win_count:
                return True
        main_diagonal = [self.board[i][i] for i in range(self.board_size)]
        if main_diagonal.count(target) == self.win_count:
            return True
        sec_diagonal = [self.board[i][self.board_size - i - 1] for i in range(self.board_size)]
        if sec_diagonal.count(target) == self.win_count:
            return True
        
        return False

    def win_screen(self, player) -> None:
        clear_terminal()
        self.draw_board()
        print(f'{self.names[player]} wins!')
    
    def round(self) -> True:
        while True:
            for player in ['X', 'O']:
                self.refresh(player)
                if self.win(player):
                    self.scores[player] += 1
                    self.win_screen(player)
                    self.reset_board()
                    return True