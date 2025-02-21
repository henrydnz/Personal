import numpy as np

class Materia:
    def __init__(self, notas: list[int], pesos: list[int], divisor: int):
        self.notas = notas
        self.pesos = pesos
        self.divisor = divisor
        self.media = self.mean()
    
    def mean(self) -> int:
        return sum(nota * peso for nota, peso in zip(self.notas, self.pesos))/self.divisor

