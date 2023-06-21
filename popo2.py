vehiculos = []

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

    if not validar_patente(patente):
        print("La patente ingresada no es válida.")
        return
    if not validar_marca(marca):
        print("La marca debe tener entre 2 y 15 caracteres.")
        return
    if not validar_precio(precio):
        print("El precio debe ser mayor a $5,000,000.")
        return

    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha_registro": fecha_registro,
        "nombre_dueno": nombre_dueno
    }

    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            print("== Información del vehículo encontrado ==")
            print("Tipo:", vehiculo["tipo"])
            print("Patente:", vehiculo["patente"])
            print("Marca:", vehiculo["marca"])
            print("Precio:", vehiculo["precio"])
            print("Multas:", vehiculo["multas"])
            print("Fecha de Registro:", vehiculo["fecha_registro"])
            print("Nombre del Dueño:", vehiculo["nombre_dueno"])
            encontrado = True
            break
    if not encontrado:
        print("Vehículo no encontrado.")

def imprimir_certificados():
    print("== Certificados de Emisión de Contaminantes, Anotaciones Vigentes y Multas ==")
    for vehiculo in vehiculos:
        print("Certificado de Emisión de Contaminantes")
        print("Patente:", vehiculo["patente"])
        print("Dueño:", vehiculo["nombre_dueno"])
        print("---")
        print("Certificado de Anotaciones Vigentes")
        print("Patente:", vehiculo["patente"])
        print("Dueño:", vehiculo["nombre_dueno"])
        print("---")
        print("Certificado de Multas")
        print("Patente:", vehiculo["patente"])
        print("Dueño:", vehiculo["nombre_dueno"])
        print("===")

def validar_patente(patente):
    # Verificar que la patente tenga un formato válido
    return True  # Implementar validación según el formato deseado

def validar_marca(marca):
    return 2 <= len(marca) <= 15

def validar_precio(precio):
    return precio > 5000000

while True:
    print("== Menú de Opciones ==")
    print("1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        grabar_vehiculo()
    elif opcion == '2':
        buscar_vehiculo()
    elif opcion == '3':
        imprimir_certificados()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
