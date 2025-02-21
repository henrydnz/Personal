# exploring classes and rpg pvp design

class Player:
    def __init__(self, hp: int, atk: int) -> None:
        self.hp = hp
        self.atk = atk

    def show(self) -> None:
        print(f"player hp: {self.hp}")
        print(f"player atk: {self.atk}")

class Goblin:
    def __init__(self, name: str, hp: int, atk: int) -> None:
        self.name = name
        self.hp = hp
        self.atk = atk
    def show(self) -> str:
        return f"{self.name} ({self.atk}atk / {self.hp}hp)"

def attack(p1: Goblin | Player , p2: Goblin | Player ) -> int:
    p2.hp-=p1.atk
    if p2.hp <= 0: return 1
    return 0

def fight(player: Player, goblin: Goblin) -> None:
    print(f"ENCOUNTER! {goblin.show()}")
    while True:
        input("press enter to attack")
        if attack(player, goblin): 
            print("goblin died")
            return 1
        if attack(goblin, player):
            player.hp = 0
            print("player died")
            return 0
        print(f"\ngoblin - {goblin.hp}hp \t VS \t player - {player.hp}hp\n")

def main(*args) -> None:
    player: Player = Player(20, 5)
    basicGoblin: Goblin = Goblin("Goblin", 20, 2)
    boss: Goblin = Goblin("Boss", 1000, 1000)
    print("========== GOBLIN FOREST ==========")
    player.show()
    input("press enter to continue\n")

if __name__ == "__main__":
    main()

