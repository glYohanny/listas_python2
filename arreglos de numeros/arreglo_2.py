import numpy as np
import random 
n=0
f=0
arregloA = np.random.randint(1000, size=(10))
print(arregloA)
lista=[]
lista2=[]

for x in arregloA:
    if x % 2 == 0:
        lista.append(x)

print(f"la cantidad de numeros pares son {len(lista)}")

for x in arregloA:
    if x % 2 != 0:
        lista2.append(x)

print(f"la suma de los elementos impares son: {np.sum(lista2)}")

for x in arregloA:
    n=n+1
    i=x%n
   if i==0:
       f=f+1
