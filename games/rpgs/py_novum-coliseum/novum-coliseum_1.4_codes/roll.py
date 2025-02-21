
from module import *
from random import randint

"""
Roll Class
Contains metohds related to random dice rolling values.
"""

class Roll:
    def __init__(self, amount: int, size: int, returnType, desc: str):
        self.amount: int = amount
        self.size: int = size
        self.returnType: sum | max = returnType
        self.desc: str = desc
        self.values: list = []

    def show(self) -> None:
        formatted_values = [
        bold(str(value)) if value == max(self.values) else str(value) 
        for value in self.values
        ]

        print_chunk(f"""
        {bold(self.desc+':')} {self.amount}d{self.size} ({','.join(n for n in formatted_values)}) 
        {bold('Total:')} {sum(self.values)}
        \033[F
        """)

    def roll(self) -> int:
        for _ in range(self.amount):
            self.values.append(randint(1, self.size))
        self.show()
        return int(self.returnType(self.values))