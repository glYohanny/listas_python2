import numpy as np
from FN import *
print ("bienvenidos a Auto Seguro\n¿Que decea?")
print("(1).-Grabar\n(2).-buscar\n(3).-imprimir certificad\n(4).-salir")
opcion=int(input("ingrece opcion"))
on=True 
while on==True:
    if opcion <5 and opcion >0:
        if opcion ==1:
            print("loginn")
        #elif opcion ==2:
        #elif opcion ==3:
        elif opcion ==4:
            print("gracias por utilizar")
            on=False