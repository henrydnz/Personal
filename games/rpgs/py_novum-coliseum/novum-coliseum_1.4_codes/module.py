import time
import sys
import os
from pathlib import Path

"""
Contains text formatting methods, animations and other useful functions
"""

def print_title() -> None:
    print(bold("""
    ███╗   ██╗ ██████╗ ██╗   ██╗██╗   ██╗███╗   ███╗
    ████╗  ██║██╔═══██╗██║   ██║██║   ██║████╗ ████║
    ██╔██╗ ██║██║   ██║██║   ██║██║   ██║██╔████╔██║
    ██║╚██╗██║██║   ██║╚██╗ ██╔╝██║   ██║██║╚██╔╝██║
    ██║ ╚████║╚██████╔╝ ╚████╔╝ ╚██████╔╝██║ ╚═╝ ██║
    ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝   ╚═════╝ ╚═╝     ╚═╝
                 COLISEUM
    """))

def print_rules() -> None:
    clear_screen()
    print_title()

    # open and read file
    file_path = Path('howToPlay.txt').resolve()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            print(file.read())
    except Exception as e:
        print(f'Error while trying to read \'{file_path.name}\' file:' )
        print(e)

    input('\nPress enter to return to Main Menu')


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def bold(text: str) -> str:
    return '\033[1m' + text + '\033[0m'

# write animation
def print_chunk(text: str, delay: float = 0.007) -> None:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# get input with '>'  char and delete line
def input_clear() -> str:
    inp = input("> ")
    print("\033[F\033[K\033[F")
    return inp

# bot '...' animation
def bot_thinking() -> None:
    for _ in range(2):  # repeat the ... animation twice
        for i in range(3):
            sys.stdout.write('.' * (i + 1) + '\r')
            sys.stdout.flush()
            time.sleep(0.3)
        sys.stdout.write('\033[K')  # clear the line
        sys.stdout.flush()

def get_valid_name(prompt: str) -> str:
    MAX_NAME_LENGTH: int = 20
    MIN_NAME_LENGTH: int = 3

    while True:
        name = input(prompt).strip()
        if len(name) == 0:
            print_chunk("Name cannot be empty. Please try again.")
        elif len(name) > MAX_NAME_LENGTH:
            print_chunk(f"Name cannot exceed {MAX_NAME_LENGTH} characters. Please try again.")
        elif len(name) < MIN_NAME_LENGTH:
            print_chunk(f"Name cannot be shorter than {MIN_NAME_LENGTH} characters. Please try again.")
        else:
            return bold(name)
