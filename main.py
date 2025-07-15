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
                print("\nIngresar Producto")
                codigo_producto = input("Ingrese el codigo del producto: ")
                if codigo_producto in productos:
                    print("El codigo ya existe")
                else:
                    nombre_producto = input("Ingrese el nombre del producto: ")
                    seleccion_categoria = int(input("Ingrese el categoria del producto (1. Hombre, 2.Mujer o 3.Niño): "))
                    if seleccion_categoria == 1:
                        categoria_producto = "Hombre"
                    elif seleccion_categoria == 2:
                        categoria_producto = "Mujer"
                    elif seleccion_categoria == 3:
                        categoria_producto = "Niño"
                    else:
                        print("La categoria no existe")
                    talla=input("Ingrese la Talla: ")
                    precio=float(input("Ingrese el precio unitario del producto: "))
                    if precio>0:
                        stock=int(input("Ingrese el stock del producto: "))
                        if stock>0:
                            productos[codigo_producto]={"nombre_producto":nombre_producto, "categoria_producto":categoria_producto,
                                                        "talla":talla, "precio":precio, "stock":stock}
                            print(f"Prodcuto {nombre_producto} ingresado correctamente")
                        else:
                            print("Stock debe ser mayor a 0")
                    else:
                        print("Precio ingresado debe ser mayor a 0")
            case 2:
                print("\nLista de Productos:")
                for codigo_producto, producto in productos.items():
                    print(f"\nCodigo del producto: {codigo_producto}")
                    print(f"Nombre del producto: {producto['nombre_producto']}")
                    print(f"Categoria del producto: {producto['categoria_producto']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    print("----------------------------")
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