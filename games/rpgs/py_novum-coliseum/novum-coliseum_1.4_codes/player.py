from module import *
from roll import Roll

"""
Player class
Contains Player stats, actions and attack/defense system related methods.
"""

class Player:
    def __init__(self, name, max_hp: int = 30) -> None:
        self.name: str = name
        self.MAX_HP = max_hp
        self.hp: int = max_hp
        self.opponent: Player | None = None

    def take_damage(self, damage_points) -> None:
        damage_points_formatted: str = bold(str(damage_points))
        print_chunk(f'{self.name} deals {damage_points_formatted} of damage on {self.opponent.name}')

        # prevents negative HP value
        self.hp = max(self.hp - damage_points, 0)
    
    def is_alive(self) -> bool:
        return self.hp > 0
    
    def show_hp(self) -> None:
        # HP max right padding amount
        max_padding: int = 30
        
        # HP right padding, relative to name lengths (keeps strings aligned)
        player1_padding: str = ' ' * (max_padding - len(self.name))
        player2_padding: str = ' ' * (max_padding - len(self.opponent.name))

        # define HP strings
        player1_hp: str = bold(str(self.hp))
        player2_hp: str = bold(str(self.opponent.hp))
        player1_string: str = f'{self.name}{player1_padding}{player1_hp} HP'
        player2_string: str = f'{self.opponent.name}{player2_padding}{player2_hp} HP'

        # display info
        print_chunk(f"""
        {player1_string}
        {player2_string}
        """)
    
    def handle_hp(self) -> None:
        if self.opponent.is_alive(): 
            self.show_hp()
        else:
            print_chunk(bold(f'{self.name} defeats {self.opponent.name}!'))

    def deal_crit_atk(self) -> None:
        print_chunk(f'{self.name} gets Critical Attack!\n')

        damage_points: int = Roll(3, 8, sum, 'Critical Damage').roll()

        self.opponent.take_damage(damage_points)

    def deal_normal_atk(self, defense_points) -> None:
        defense_points: str = bold(str(defense_points))
        print_chunk(f'{self.opponent.name} gets {defense_points} DP. {self.name} attacks!')
        
        damage_points: int = Roll(2, 8, sum, 'Damage').roll()

        self.opponent.take_damage(damage_points)
    
    def deal_crit_defense_points(self) -> None:

        MIN_CRIT_DMG: int = 2
        MAX_CRIT_DMG: int = 20

        multiplier: float = 1 - (self.hp / self.MAX_HP)
        damage_points: float = MIN_CRIT_DMG + (MAX_CRIT_DMG - MIN_CRIT_DMG) * multiplier
        damage_points: int = int(damage_points)

        damage_points_formatted: str = bold(str(damage_points))
        print_chunk(f'{self.opponent.name} gets {bold('Critical Defense')} and deals {damage_points_formatted} of damage from Reflected Attack.')

        self.take_damage(damage_points)
        
    def roll_defense(self, attack_points) -> None:
        attack_points_formatted: str = bold(str(attack_points))
        print_chunk(f"{self.name} gets {attack_points_formatted} AP.")

        defense_points: int = Roll(2, 20, max, 'Defense').roll()

        if defense_points == 20: 
            self.deal_crit_defense_points()
        elif attack_points < defense_points:
            defense_points_formatted: str = bold(str(defense_points))
            print_chunk(f'{self.opponent.name} gets {defense_points_formatted} DP. Attack was defended successfully!')
        else:
            self.deal_normal_atk(defense_points)
        
    def attack_calculate(self, attack_points) -> None:
        if attack_points == 20: 
            self.deal_crit_atk()
        else:
            self.roll_defense(attack_points)

        self.handle_hp()

    def attack(self) -> int:
        attack_points: int = Roll(2, 20, max, 'Attack').roll()
        self.attack_calculate(attack_points)

