"""
Sistema de Gestión de Ventas para Mini Juguetería.

Versión: 1.0
Línea base: LB-001
"""


productos = []


def registrar_producto():
    """Registra un producto en memoria."""
    print("\n--- Registrar producto ---")

    codigo = input("Código: ").strip()

    if buscar_producto(codigo):
        print("Error: ya existe un producto con ese código.")
        return

    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Error: precio o stock inválido.")
        return

    if not codigo or not nombre or not categoria:
        print("Error: los campos son obligatorios.")
        return

    if precio < 0 or stock < 0:
        print("Error: precio y stock no pueden ser negativos.")
        return

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
    }

    productos.append(producto)
    print("Producto registrado correctamente.")
    """Registra un producto en memoria."""
    print("\n--- Registrar producto ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Error: precio o stock inválido.")
        return

    if precio < 0 or stock < 0:
        print("Error: precio y stock no pueden ser negativos.")
        return

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
    }

    productos.append(producto)
    print("Producto registrado correctamente.")


def consultar_productos():
    """Muestra los productos registrados."""
    print("\n--- Productos disponibles ---")

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(
            f"Código: {producto['codigo']} | "
            f"Nombre: {producto['nombre']} | "
            f"Categoría: {producto['categoria']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Stock: {producto['stock']}"
        )


def calcular_total():
    """Calcula el total de una venta simple."""
    print("\n--- Calcular total de venta ---")

    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Error: datos inválidos.")
        return

    if precio < 0 or cantidad <= 0:
        print("Error: valores no permitidos.")
        return

    total = precio * cantidad

    print(f"Total de la venta: ${total:.2f}")


def mostrar_menu():
    """Muestra el menú principal."""
    while True:
        print("\n================================")
        print(" MINI JUGUETERÍA - VENTAS")
        print("================================")
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Calcular total de venta")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            calcular_total()
        elif opcion == "4":
            print("Sistema finalizado.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    mostrar_menu()

    def buscar_producto(codigo):
    """Busca un producto por su código."""
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None