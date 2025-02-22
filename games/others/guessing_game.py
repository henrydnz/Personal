# simple game about guessing a number between 0 ans 100

from random import randint

def eraseLines(count) -> None:
    print(f"\033[{count}A\033[J")

class Game:
    
    rand_number: int = randint(0,100)
    tries: int = 0
    
    def guess(self) -> None:
        while not (_guess := input("enter your guess:\n")).isnumeric():
            print("not a number")
        self.tries+=1
        return int(_guess)
    
    def round(self) -> int:
        while not (_guess := self.guess()) == self.rand_number:
            eraseLines(2)
            print("Secret number is", "below" if _guess > self.rand_number else "above", f"{_guess}!")
        print(f"You win! Secret number was {self.rand_number}")
        return self.tries

def play() -> None:
    current_game: Game = Game()
    score = current_game.round()
    return score

def main() -> None:
    max_score = 0
    while not input("enter to play"):
        score = play()
        max_score = max(score, max_score)
        print(f"max score: {max_score}")

if __name__ == "__main__":
    main()
