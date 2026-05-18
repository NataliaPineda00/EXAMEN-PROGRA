#CRUD DE TABLAS DE MULTIPLICAR CON CICLO FOR Y CRUD
#REGISTROS
tablas_guardadas = []

while True:

    print("\n----- CRUD TABLAS DE MULTIPLICAR -----")
    print("1. Crear tablas")
    print("2. Leer registros")
    print("3. Actualizar registros")
    print("4. Eliminar registros")

#INGRESO DE DATOS
    limite_tablas = int(input("Ingrese el límite de tablas: "))
    limite_numeros = int(input("Ingrese el límite de números: "))

    #REGISTRO DE DATOS
    datos = {
        "tablas": limite_tablas,
        "numeros": limite_numeros
    }

    tablas_guardadas.append(datos)
    print("\nTABLAS DE MULTIPLICAR\n")

     #IMPLEMENTACION DE CICLO FOR
    for tabla in range(1, limite_tablas + 1):
        print(f"----TABLA {tabla}----")

        for numero in range(1, limite_numeros + 1):
            resultado = tabla * numero
            print(f"{tabla} x {numero} = {resultado}")

            print()
#LECTOR DE DATOS
    if len(tablas_guardadas) == 0:
        print("No hay registros guardados.")
    else:
        print("\nREGISTROS GUARDADOS")

        for i, dato in enumerate(tablas_guardadas):

            print(f"{i+1}. "
                  f"Tablas: {dato['tablas']} | "
                  f"Números: {dato['numeros']}")

#ACTUALIZADOR DE DATOS
    if len(tablas_guardadas) > 0:

        opcion = int(input("Seleccione el registro a actualizar: ")) - 1

        if 0 <= opcion < len(tablas_guardadas):
            nuevos_tablas = int(input("Nuevo límite de tablas: "))
            nuevos_numeros = int(input("Nuevo límite de números: "))

            tablas_guardadas[opcion]["tablas"] = nuevos_tablas
            tablas_guardadas[opcion]["numeros"] = nuevos_numeros

            print("Registro actualizado correctamente.")

        else:
            print("Opción inválida.")

#BORRAR DATOS
    if len(tablas_guardadas) >0:
        opcion = int(input("Seleccione el registro a eliminar: ")) - 1

        if 0 <= opcion < len(tablas_guardadas):

            tablas_guardadas.pop(opcion)

            print("Registro eliminado correctamente.")

        else:
            print("Opción inválida.")