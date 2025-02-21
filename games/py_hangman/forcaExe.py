# hangman's game I did when i didnt know python classes
# (still dont know lol)

import random as rd
from os import name, system
from time import sleep
from typing import Literal

# clear terminal command variants
def clear() -> None:
    if name == 'nt':
        _ = system('cls') # windows
    else:
        _ = system('clear') # other

# string bolder
def boldStr(*strings: str | list) -> str: 
    for string in strings:
        return f'\033[1m{string}\033[0m'

#  wlist[0] -> pt words list
#  wlist[1] -> en words list
wlist = [ 
    [
    'abacate', 'abajur', 'abelha', 'alface', 'berinjela', 
    'bicicleta', 'bola', 'bolo', 'borboleta', 'cachorro', 
    'cadeira', 'cama', 'caneca', 'capivara', 'computador', 
    'copo', 'coxinha', 'dado', 'dente', 'desafio', 
    'dicionario', 'dinossauro', 'elefante', 'escola', 'escova', 
    'escova de dente', 'espelho', 'faca', 'foca', 'foguete', 
    'fruta', 'futebol', 'gato', 'gaveta', 'girafa', 
    'girassol', 'guitarra', 'hamburguer', 'harpa', 'helice', 
    'hipopotamo', 'iate', 'igreja', 'ilha', 'internet', 
    'isca', 'jacare', 'janela', 'jogo', 'joia', 
    'lampiao', 'lapis', 'laranja', 'laranjeira', 'maca', 
    'maca do amor', 'mamao', 'margarida', 'mochila', 'navio', 
    'neve', 'notebook', 'nuvem', 'onibus', 'orquestra', 
    'ovo', 'palhaco', 'pao', 'pato', 'piramide', 
    'queijadinha', 'queijo', 'queimada', 'quero quero', 'raposa', 
    'ratoeira', 'relampago', 'relogio', 'rua', 'salada', 
    'sapato', 'sorvete', 'sorveteria', 'tambor', 'tartaruga', 
    'tesouro', 'travesseiro', 'unicornio', 'urna', 'urso', 
    'urubu', 'vaso', 'vassoura', 'vela', 'xadrez', 
    'xicara', 'yakisoba', 'zebra', 'ziper', 'zoologico'
    ],
    [
    'adventure', 'airplane', 'apple', 'astronaut', 'coconut' 
    'ball', 'balloon', 'banana', 'butterfly', 'ant', 
    'carrot', 'castle', 'cat', 'caterpillar', 'challenge', 
    'cheesecake', 'computer', 'crocodile', 'daisy', 'diamond', 
    'dog', 'dragon', 'drum', 'egg', 'elephant', 
    'cucumber', 'building', 'feather', 'fish', 'forest', 
    'globe', 'guitar', 'piano', 'hammer', 'hat', 
    'hippopotamus', 'house', 'ice cream', 'icecream', 'igloo', 
    'internet', 'island', 'jacket', 'jelly', 'jellyfish', 
    'kangaroo', 'king', 'kite', 'laptop', 'lemon', 
    'lemonade', 'lightning', 'lion', 'monkey', 'moon', 
    'mouse', 'necklace', 'nest', 'notebook', 'octopus', 
    'orange', 'salt', 'orchestra', 'owl', 'parrot', 
    'penguin', 'pizza', 'pyramid', 'queen', 'quilt', 
    'rainbow', 'rain', 'robot', 'rocket', 'skateboard', 
    'snowflake', 'star', 'sunflower', 'telescope', 'tiger', 
    'tree', 'umbrella', 'game', 'horse', 'unicorn', 
    'van', 'violin', 'volcano', 'waterfall', 'watermelon', 
    'whale', 'x ray', 'boat', 'xylophone', 'yacht', 
    'yak', 'yo yo', 'zebra', 'rabbit', 'tomato'
    ]
]

# choose game idiom
def set_idiom() -> int:
    while True:
        # decr
        print(f'{boldStr('Idioms:')}\n\n'
              'Portuguese (1)\n'
              'English (2)\n')
        idiom = input('Set idiom (1, 2): ')
        clear()
        # inp filter
        if not idiom.isdigit() or int(idiom) not in (1, 2):
            print(f'Invalid option: {boldStr(f'\'{idiom}\'')}\n')
            continue
        else:
            idiom = int(idiom)
            print(f'The idiom was set to {boldStr('English')}.' if idiom == 2 else
                  f'O idioma escolhido foi {boldStr('Português')}.')
            print('=======================')
            return idiom

# choose game difficulty
def set_diff(inEnglish: bool) -> Literal[7] | Literal[5] | Literal[3] | Literal[1]:
    while True:
        # descrip
        print(
            f'{boldStr('Difficulties:')}\n\n'
            'Easy (a): 7 tries\n'
            'Medium (b): 5 tries\n'
            'Hard (c): 3 tries\n'
            'Impossible (d): 1 try\n'
            if inEnglish else
            f'{boldStr('Dificuldades:')}\n\n'
            'Fácil (a): 7 tentativas\n'
            'Médio (b): 5 tentativas\n'
            'Difícil (c): 3 tentativas\n'
            'Impossível (d): 1 tentativa\n'
        )
        difficulty = input('Select difficulty (a, b, c, d): ' if inEnglish else 
                            'Selecione a dificuldade (a, b, c, d): ')
        clear()

        # filter
        if not difficulty.isalpha() or difficulty.lower() not in ('a', 'b', 'c', 'd'): 
            print(f'Invalid option: {boldStr(f'\'{difficulty}\'')}\n' if inEnglish else
                  f'Opção inválida: {boldStr(f'\'{difficulty}\'')}\n')
        # options
        elif difficulty == 'a': 
            print(f'Chosen difficulty: {boldStr('-Easy-')}' if inEnglish else
                  f'Dificuldade escolhida: {boldStr('-Fácil-')}')
            return 7
        elif difficulty == 'b':
            print(f'Chosen difficulty: {boldStr('-Medium-')}' if inEnglish else 
                  f'Dificuldade escolhida: {boldStr('-Médio-')}')
            return 5
        elif difficulty == 'c':
            print(f'Chosen Difficulty: {boldStr('-Hard-')}' if inEnglish else 
                  f'Dificuldade escolhida: {boldStr('-Difícil-')}')
            return 3
        elif difficulty == 'd':
            print(f'Chosen difficulty: {boldStr('-Impossible-')}\n{boldStr('You can\'t fail.')} Good luck! :)\n' if inEnglish else 
                  f'Dificuldade escohida: {boldStr('-Impossível-')}\n{boldStr('Você não pode errar.')} Boa sorte! :)\n')
            return 1

# random word choosing
def set_word(inEnglish: bool) -> str:
    #  wlist[ True = 1 (english) ]  |  wlist[ False = 0 (portuguese) ]
    return rd.choice(wlist[int(inEnglish)])

# display words ( _ _ _ a _ )
def display_word(word: str, guessed_letters: list):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# main game function
def game(inEnglish: bool) -> int:

    word = set_word(inEnglish) # setting secret word
    tries = set_diff(inEnglish) # setting tries count
    guessed_letters = [' '] # list with all guessed letters (containing space for space characters to print)
    wrong_guesses = 0 # function output: show wrong guesses records after the game ends

    # main loop
    while tries > 0:
        # descript
        print('=================\n') # spacer
        print(display_word(word, guessed_letters)) # secret word
        print(f'Remaining tries: {tries}\n' if inEnglish else 
              f'Tentativas faltando: {tries}\n')
        letter = input('Type a guess: ' if inEnglish else 
                       'Escreva uma letra: ').lower()
        clear() # update

        # filter wrong input
        if len(letter) != 1 or not letter.isalpha(): 
            print('Incorrect input. Type exactly one letter, please.'if inEnglish else 
                  'Entrada incorreta. Escreva exatamente uma letra, por favor.')
        # filter repeated letters
        elif letter in guessed_letters:
            print(f'You already guessed the letter \'{letter}\'!' if inEnglish else 
                  f'Você já escreveu a letra \'{letter.upper()}\'!')
        # letter is right
        elif letter in word:
            if tries > 1:
                print(f'Nice! The letter \'{letter.upper()}\' is in the word!' if inEnglish else
                      f'Boa! A letra \'{letter.upper()}\' está na palavra!')
            guessed_letters.append(letter)
        # letter is wrong
        else:
            if tries > 1:
                print(f"Try again... The letter \'{letter.upper()}\' isn't in the word." if inEnglish else
                      f"Tente de novo... A letra \'{letter.upper()}\' não está na palavra.")
            guessed_letters.append(letter)
            # counters updating
            wrong_guesses += 1
            tries -=1

        # winning message
        if set(word).issubset(set(guessed_letters)):
            print(f'{boldStr(
                '\n========\n'
                'You Win!\n'
                '========\n')}'
                f'\nWord: {boldStr(word)}\n'
                f'Wrong Guesses: {wrong_guesses}\n'
                if inEnglish else
                f'{boldStr(
                '\n============\n'
                'Você Ganhou!\n'
                '============\n')}'
                f'\nPalavra: {boldStr(word)}\n'
                f'Erros: {wrong_guesses}\n')
            
            # return counter recording
            return wrong_guesses
    
    # tries are over message
    else: 
        print(f"Your tries are over... The word was {word}.\nDon't worry, you can do better!" if inEnglish else
              f'Suas tentativas acabaram... A palavra era {word}.\nNão se preocupe, você consegue!')
        return False # else it outputs NoneType
    
# game initialization and play again
best = []
def play(best: list) -> None:
    # initializaton
    inEnglish: bool = set_idiom() == 2
    best.append(game(inEnglish)) # initializes and append wrong recording
    # game end: display record
    best_filtered = [guess_count for guess_count in best if guess_count is not False]
    if best_filtered:
        print(f'Record: {min(best)}' if inEnglish else f'Recorde: {min(best)}')
    else: 
        print('Record: No successful games played yet.' if inEnglish else 
              'Recorde: Ainda sem partidas ganhas salvas.')
    print('==================')

    # play again loop
    while True:
        play_again_input = input('Do you want to play again? (y/n) ' if inEnglish else
                                 'Você quer jogar de novo? (y/n) ').lower()
        # filter
        if not play_again_input.isalpha() or play_again_input not in ('y', 'n'):
            print(f'Invalid input. (\'{play_again_input}\')' if inEnglish else
                  f'Opção inválida. (\'{play_again_input}\')')
        # options
        elif play_again_input == 'y':
            clear()
            play(best)
        else:
            print('=======================')
            print('Thank you for playing!' if inEnglish else 'Obrigado por jogar!')
            print('=======================')
            print('Closing...' if inEnglish else 'Fechando...')
            sleep(1)
            break
            
# execute
play(best)