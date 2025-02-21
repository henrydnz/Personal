from game import Game
from module import *

def main_menu() -> None:
    while True:
        clear_screen()
        print_title()
        
        print(f"""
        {bold('1')}  Multiplayer
        {bold('2')}  Single Player (Novum Bot)
        {bold('3')}  How to Play
        {bold('4')}  Exit Game
        """)

        choice = input_clear()
        
        match choice:
            case '1':
                run(bot=False)
            case '2':
                run(bot=True)
            case '3':
                print_rules()
            case '4':
                print("\nThanks for playing!")
                break
            case _:
                input("        Not a valid option! press Enter to continue...")

def run(bot: bool) -> None:
    clear_screen()

    if not bot:
        print_chunk(bold("           Player vs Player           \n"))
        name1 = get_valid_name('Player 1: ')
        name2 = get_valid_name('Player 2: ')

        clear_screen()
        game = Game(name1, name2)

    else:
        print_chunk(bold("           Player vs Novum Bot           \n"))
        name1 = get_valid_name('Player: ')
    
        clear_screen()
        game = Game(name1, bold("Novum Bot"), is_bot=True)

    while game.round():
        pass
    
    input(bold("\nPress Enter to return to main menu..."))


if __name__ == "__main__":
    main_menu()