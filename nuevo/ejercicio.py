import numpy as np 
tipo=[]
patente=[]
marca=[]
precio=[]
monto=[]
fecha=[]
multa=[[monto],[fecha]]
fecha_registro=[]
nom_dueño=[]
arreglo1=[[tipo],[patente],[marca],[precio],[multa],[fecha_registro],[nom_dueño],[fecha_registro]]
arreglo1=np.array(arreglo1)
print(arreglo1[1][0])
on=True
while on==True:
    op=int(input("ingrese opcion deseada\n(1)Grabar\n(2)Buscar\n(3)Imprimir certificado\n(4)Salir\n"))
    if op>0 and op<5:
        if op==1:
            print("omomomo")
        if op==2:
            print("omomomo")
        if op==3:
            print("omomomo")
        if op==4:
            print("asta pronto")
            on=False