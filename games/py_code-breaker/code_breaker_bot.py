# password guesser
# think of a password
# say the program how numbers it got right:
# - in the right place as your password
# - in the wrong place as your password

import itertools 
from random import choice
from os import name, system as sys

def c() -> None: sys('cls' if name == 'nt' else 'clear')

# filter possibilities
def filter(guess, x, y, possible, size) -> None:
    filtered = []
    for n in possible:

        if n == guess:
            continue

        nx = right_count(n, guess, size)
        if nx != x:
            continue

        ny = wrong_count(n, nx, guess)
        if ny != y:
            continue

        filtered.append(n)

    possible[:] = filtered

def right_count(n, g, sz) -> int:
    return sum(1 for i in range(sz) if g[i] == n[i])

def wrong_count(n, nx, g):# -> Any:
    g_count = {d: g.count(d) for d in set(g)}           # freq of digits in guess
    n_count = {d: n.count(d) for d in set(n)}           # freq of digits in n
    total = sum(min(g_count.get(d, 0), n_count.get(d, 0)) for d in g_count) 
    return total - nx

def lose() -> None:
    print('\nSorry... I couldn\'t guess your password.')

def win(g) -> None:
    print(f'\nI won! Your password was {g}.')

def game() -> None:

    print('Imagine any password, made up of digits only! I will guess it.\n')
    int_range: int = int(input('> Enter the largest digit in your password (0-9).\n'))
    str_range: str = ''.join([str(d) for d in range(0, int_range+1)])
    size: int = int(input('> Enter the number of digits in your password. If it has more than 8, it will take me a long time ;(\n'))
    all: list[str] = [''.join(p) for p in itertools.product(str_range, repeat=size)]
    possible: list[str] = all


    c()

    while True:

        if len(possible) == 0:
            lose()
            break

        if len(possible) == 1:
            op = input(f'\n{possible[0]} is my guess! Did I get it right? (y/n) ')
            if op == 'y': 
                win(possible[0])
            else:
                lose()
            break

        guess: str = choice(possible)
        op: str = input(f'\nIs your password... {guess}? (y/n) - ')

        if op == 'y':
            win(guess)
            break

        x = int(input('> How many digits are in the correct position? - '))
        y = int(input('> How many digits are in the wrong position? - '))

        if x == size: 
            win(guess)
            print('You said it wasn’t the one... you lied to me.')
            break

        filter(guess, x, y, possible, size)

    print('\nIt was fun playing with you!\n')

def main() -> None:
    c()
    while True:
        input('Press Enter to play Code Breaker. \n')
        c()
        game()

main()

        