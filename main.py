def Menu():
    print("--- MENU ---")
    print("1. Ingresar Producto")
    print("2. Lista de Productos")
    print("3. Buscar Producto")
    print("4. Valor Total del Inventario")
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
                buscar_producto = input("Ingrese el codigo del producto: ")
                if buscar_producto in productos:
                    print("\nProducto encontrado")
                    print(f"Nombre del producto: {productos[buscar_producto]['nombre_producto']}")
                    print(f"Categoria del producto: {productos[buscar_producto]['categoria_producto']}")
                    print(f"Talla: {productos[buscar_producto]['talla']}")
                    print(f"Precio: {productos[buscar_producto]['precio']}")
                    print(f"Stock: {productos[buscar_producto]['stock']}")
                else:
                    print("Producto no existe")
            case 4:
                print("Valor Inventario")
                valor_inventario = 0
                for inventario in productos.values():
                    print("--------------------------------------------------------------------------------------------------------------------------")
                    print(f"Nombre del producto: {inventario['nombre_producto']} || Talla: {inventario['talla']} || Precio Unitario: Q{inventario['precio']} || Stock: {inventario['stock']}")
                    valor_inventario += inventario['precio'] * inventario['stock']
                print("-----------------------------------------------------------------")
                print(f"Valor Total del Inventario: Q{valor_inventario}")
            case 5:
                cantidad_hombre = 0
                cantidad_mujer = 0
                cantidad_baby = 0
                for producto in productos.values():
                    if producto['categoria_producto'] == "Hombre":
                        cantidad_hombre += producto['stock']
                    elif producto['categoria_producto'] == "Mujer":
                        cantidad_mujer += producto['stock']
                    elif producto['categoria_producto'] == "Niño":
                        cantidad_baby += producto['stock']
                print("\nCantidad Producto por Categoria:")
                print(f"Hombre: {cantidad_hombre} || Mujer: {cantidad_mujer} || Niño: {cantidad_baby}")
            case 6:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion no valida")
    except Exception:
        print("Debe ingresar solo numeros")