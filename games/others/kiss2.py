# multipliayer  game.
# two persons. 
# if both wanna kiss then they will.
# else they wont.
# play it.

from os import system, name

clear: str = 'cls' if name == 'nt' else 'clear'

def get_names() -> list[str]:
    names = []
    for i in range(2):
        name: str = input(f'person {i+1}, what\'s your name?\n')
        names.append(name)
        system(clear)
    return names

def get_responses(names) -> list[bool]:
    responses = []
    for i in range(2):
        response: str = input(f'{names[i]}, do you wanna kiss {names[i-1]}? (y/n)')
        responses.append(response == 'y')
        system(clear)
    return responses

def compute(names, responses) -> None:
    if all(responses):
        print('both are kissing! :)')
    elif any(responses):
        print(f'no kisses... {names[0] if not responses[0] else names[1]} don\'t want kisses. :(')
    else: 
        print('no one wanna kiss... ;(')
        
    print()

def main() -> None:
    system(clear)
    while(input('play? (y/n)') == 'y'):
        system(clear)
        names = get_names()
        responses = get_responses(names)
        compute(names, responses)

if __name__ == "__main__":
    main()