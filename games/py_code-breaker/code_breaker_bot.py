import itertools 
from random import choice
from os import name, system as sys

def c(): sys('cls' if name == 'nt' else 'clear')

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

def right_count(n, g, sz):
    return sum(1 for i in range(sz) if g[i] == n[i])

def wrong_count(n, nx, g):
    g_count = {d: g.count(d) for d in set(g)}   # freq of digits in guess
    n_count = {d: n.count(d) for d in set(n)}           # freq of digits in n
    total = sum(min(g_count.get(d, 0), n_count.get(d, 0)) for d in g_count) 
    return total - nx

def lose():
    print('\nDesculpe... Eu não consegui adivinhar sua senha.')

def win(g):
    print(f'\nGanhei! Sua senha era {g}.')

def game() -> None:

    print('Imagine uma senha qualquer, composta apenas por dígitos! Eu vou adivinhar.\n')
    int_range: int = int(input('> Digite o maior dígito da sua senha (0-9).\n'))
    str_range: str = ''.join([str(d) for d in range(0, int_range+1)])
    size: int = int(input('> Digite a quantidade de dígitos da sua senha. Se ela tiver mais que 8, eu vou demorar muito ;(\n'))
    all: list[str] = [''.join(p) for p in itertools.product(str_range, repeat=size)]
    possible: list[str] = all

    c()

    while True:

        if len(possible) == 0:
            lose()
            break

        if len(possible) == 1:
            op = input(f'\n{possible[0]} é o meu chute! Acertei? (s/n) ')
            if op == 's': 
                win(possible[0])
            else:
                lose()
            break

        guess: str = choice(possible)
        op: str = input(f'\nSua senha é... {guess}? (s/n) - ')

        if op == 's':
            win(guess)
            break

        x = int(input('> Quantos números estão na posição correta? - '))
        y = int(input('> Quantos números estão na posição errada? - '))

        if x == size: 
            win(guess)
            print('tu disse que nao era cara... tu mentiu pra mim')
            break

        filter(guess, x, y, possible, size)

    print('\nFoi divertido jogar com você!\n')

def main() -> None:
    c()
    while True:
        input('Pressione Enter para jogar Akisenhator\n')
        c()
        game()

main()

        