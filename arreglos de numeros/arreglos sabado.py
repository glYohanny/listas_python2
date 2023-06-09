import numpy as np
import random 

arregloA = np.random.randint(500, size=(100))
lista = []

print("Los números aleatorios son: ",arregloA)

for x in range(len(arregloA)):
    if x % 2 == 0:
        lista.append(arregloA[x])

print("Los números en los índices pares son: ", lista)

arreglo_cop = arregloA.copy()
arreglo_cop1 = arregloA.copy()
arreglo_cop.sort()


numero = arreglo_cop[-1]

print("El número mínimo es:", arreglo_cop[0])
print("El número máximo es:", arreglo_cop[-1])

indice = np.where(arregloA == numero)[0][0]
print("El índice del número máximo en arreglo1 es:", indice)
arreglo_cop1=arreglo_cop1*3
print("hola",arreglo_cop1)
print(np.sum(arreglo_cop1))
