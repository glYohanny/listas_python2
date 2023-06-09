import numpy as np

vehiculos = np.empty((0, 7), dtype=object)  # Arreglo NumPy para almacenar los datos de los vehículos

def grabar_vehiculo():
    print("== Ingresar datos del vehículo ==")
    tipo = input("Tipo de vehículo: ")
    patente = input("Patente: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    multas = []
    while True:
        opcion = input("¿Agregar multa? (S/N): ")
        if opcion.upper() == 'S':
            monto = float(input("Monto de la multa: "))
            fecha = input("Fecha de la multa (YYYY-MM-DD): ")
            multas.append({"monto": monto, "fecha": fecha})
        else:
            break
    fecha_registro = input("Fecha de registro del vehículo (YYYY-MM-DD): ")
    nombre_dueno = input("Nombre del dueño: ")

    vehiculo = np.array([[tipo, patente, marca, precio, multas, fecha_registro, nombre_dueno]], dtype=object)
    if not validar_patente(patente):
        print("La patente ingresada no es válida.")
        return
    if not validar_marca(marca):
        print("La marca debe tener entre 2 y 15 caracteres.")
        return
    if not validar_precio(precio):
        print("El precio debe ser mayor a $5,000,000.")
        return

    vehiculos = np.concatenate((vehiculos, vehiculo), axis=0)
    print("Vehículo registrado exitosamente.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo[1] == patente:
            print("== Información del vehículo encontrado ==")
            print("Tipo:", vehiculo[0])
            print("Patente:", vehiculo[1])
            print("Marca:", vehiculo[2])
            print("Precio:", vehiculo[3])
            print("Multas:", vehiculo[4])
            print("Fecha de Registro:", vehiculo[5])
            print("Nombre del Dueño:", vehiculo[6])
            encontrado = True
            break
    if not encontrado:
        print("Vehículo no encontrado.")

def imprimir_certificados():
    print("== Certificados de Emisión de Contaminantes, Anotaciones Vigentes y Multas ==")
    for vehiculo in vehiculos:
        print("Certificado de Emisión de Contaminantes")
        print("Patente:", vehiculo[1])
        print("Dueño:", vehiculo[6])
        print("---")
        print("Certificado de Anotaciones Vigentes")
        print("Patente:", vehiculo[1])
        print("Dueño:", vehiculo[6])
        print("---")
        print("Certificado de Multas")
        print("Patente:", vehiculo[1])
        print("Dueño:", vehiculo[6])
        print("===")

def validar_patente(patente):
    # Verificar que la patente tenga un formato válido
    # Ejemplo: AA123BB
    if len(patente) != 7:
        return False
    if not patente[:2].isalpha() or not patente[2:5].isdigit() or not patente[5:].isalpha():
        return False
    return True
