from materia import Materia

calculo = Materia([81,81,0,0,0,0],[10,15,25,25,10,15],100)

ga = Materia([10,73,10,66,10,70,5,10,77,10],[1 for _ in range(10)],6)
print(calculo.mean())
print(ga.mean())