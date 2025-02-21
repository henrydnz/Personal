from ast import main
from bot import Bot
from module import *
from player import Player
from roll import Roll

"""
Game Class
Contains methods related to game funcionality, data, rounds, choosing and general logic.
"""

class Game:
    def __init__(self, name1, name2, is_bot=False) -> None:
        self.player1 = Player(name1)
        self.player2 = Bot(name2) if is_bot else Player(name2)
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1
        self.dtp = 8
        self.MAX_ATK_DIST = 3
        self.MAX_DTP = 12
        self.is_bot = is_bot

    def get_actions(self) -> None:
        print_chunk(f"""
        \033[F
        {
            f'{bold('1')}  Run forward'
            if not self.dtp == 1 
            else '\033[F'
        }
        {
            f'{bold('2')}  Run backwards'
            if not self.dtp == self.MAX_DTP 
            else '\033[F'
        }
        { 
            f'{bold('3')}  Attack'
            if self.can_attack()
            else '\033[F'
        }
        """)

    def bot_choosing(self, target) -> None:
        bot_thinking()
        action: int = target.choose_action(self)
        print_chunk(f'\n{target.name} chooses to')

        match action:
            case '1': 
                print_chunk(bold('Run forward'))
                self.run_forward(target)
            case '2':
                print_chunk(bold('Run backwards'))
                self.run_backwards(target)
            case '3':
                print_chunk(bold('Attack'))
                target.attack()

    def player_choosing(self, target) -> None:
        print(f'\n{target.name}, choose your action.')
        self.get_actions()
        while True:
            action: str = input_clear()
            match action:
                case '1':
                    if self.can_run_forward():
                        self.run_forward(target)
                        break
                    else:
                        self.action_error()
                case '2':
                    if self.can_run_backwards():
                        self.run_backwards(target)
                        break
                    else: 
                        self.action_error()
                case '3':
                    if self.can_attack(): 
                        target.attack()
                        break
                    else:
                        self.action_error()
                case _: 
                    self.action_error()

    def action(self, target) -> None:
        if isinstance(target, Bot):
            self.bot_choosing(target)
        else:
            self.player_choosing(target)

    def action_error(self) -> None:
        print_chunk(bold('Not a valid option!'))

    def can_attack(self) -> bool:
        return self.dtp <= self.MAX_ATK_DIST
    
    def can_run_backwards(self) -> bool:
        return self.dtp < self.MAX_DTP
        
    def can_run_forward(self) -> bool:
        return self.dtp > 1
    
    def run_backwards(self, target) -> None:
        steps: int = Roll(2, 4, sum, 'Steps').roll()
        old_distance: int = self.dtp

        self.dtp = min(old_distance + steps, self.MAX_DTP)
        steps = self.dtp - old_distance

        print_chunk(f'{target.name} runs {steps} steps backwards.')

        self.get_distance()

    def run_forward(self, target) -> None:
        steps: int = Roll(2, 4, sum, 'Steps').roll()
        old_distance: int = self.dtp
        
        steps = min(steps, old_distance - 1)
        self.dtp = max(old_distance - steps, 1)

        print_chunk(f'{target.name} runs {steps} steps forward.')

        self.get_distance()

    def get_distance(self) -> None:
        if self.dtp == 1: 
            print_chunk('Players reached minimum distance of one step.')
        elif self.dtp == self.MAX_DTP: 
            print_chunk(f'Players reached maximum distance of {self.MAX_DTP} steps.')
        else: 
            print_chunk(f'players are now {self.dtp} steps apart.')

    def round(self) -> bool:
        for player, opponent in [(self.player1, self.player2), (self.player2, self.player1)]:
            self.action(player)
            if not opponent.is_alive():
                return False
        
        return True  

