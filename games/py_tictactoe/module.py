import os

def print_inline(text: str) -> None:
    print(text, end='')

def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_line(line_count: int = 1) -> None:
    for _ in range(line_count):
        print('\033[F\033[K', end='')

def valid_board_size(input: str) -> bool:
    if not input.isdigit():
        clear_line()
        print_inline('Board size must be an integer. Please try again: ') 
        return False
    if not 2 < int(input) < 10:
        clear_line()
        print_inline('Size must be between 3 and 9. Please try again: ')
        return False
    return True

def get_board_size() -> int:
    size = input('Input board size (between 3 and 9): ')
    while not valid_board_size(size):
        size = input()
    return int(size)

def get_names() -> list[str, str]:
    name_1: str 
    name_2: str
    