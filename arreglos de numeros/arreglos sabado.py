import numpy as np
import random 

arreglo1 = np.random.randint(500, size=(100))
lista = []

print("Los números aleatorios son: ", arreglo1)

for x in range(len(arreglo1)):
    if x % 2 == 0:
        lista.append(arreglo1[x])

print("Los números en los índices pares son: ", lista)

arreglo_cop = arreglo1.copy()
arreglo_cop.sort()

numero = arreglo_cop[-1]

print("El número mínimo es:", arreglo_cop[0])
print("El número máximo es:", arreglo_cop[-1])

indice = np.where(arreglo1 == numero)[0][0]
print("El índice del número máximo en arreglo1 es:", indice)

