usuario1=1
contrasena=2
encendido=True
lista=["maxi","alex"]
deuda=[10000,2000]
while encendido ==True:
    print("(1)lista de deudores\n(2)agregar lista de deudoresn\n(3)quitar de lista de deudores\n(0)salir")
    op1=int(input("seleccione opcion "))
    if op1<5 and op1>-1: 
        if op1==1:
            for n in range(len(lista)):
              print("deudor ",lista[n]," tiene como deuda ",deuda[n])