def Menu():
    print("--- MENU ---")
    print("1. Ingresar Producto")
    print("2. Lista de Productos")
    print("3. Buscar Producto")
    print("4. Cantidad Total de Inventario")
    print("5. Cantidad de Producto por categoria")
    print("6. Salir")

productos={}
while True:
    Menu()
    opcion=int(input("Ingrese una opcion: "))
    try:
        match opcion:
            case 1:
                print("Ingresar Producto")
            case 2:
                print("Lista de Productos")
            case 3:
                print("Buscar Producto")
            case 4:
                print("Cantidad Inventario")
            case 5:
                print("Cantidad Categoria")
            case 6:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion no valida")
    except Exception:
        print("Debe ingresar solo numeros")