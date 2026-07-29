"""
Sistema de Gestión de Ventas para Mini Juguetería.

Versión: 1.0
Línea base: LB-001
"""


productos = []

import sqlite3
from pathlib import Path
from datetime import datetime

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
    """Consulta todos los productos almacenados."""
    print("\n--- Productos disponibles ---")

    with obtener_conexion() as conexion:
        registros = conexion.execute(
            """
            SELECT codigo, nombre, categoria, precio, stock
            FROM productos
            ORDER BY nombre
            """
        ).fetchall()

    if not registros:
        print("No existen productos registrados.")
        return

    for producto in registros:
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
        print("4. Actualizar stock")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            calcular_total()
        elif opcion == "4":
    codigo = input("Código del producto: ").strip()

    try:
        cantidad = int(input("Cantidad a modificar: "))
    except ValueError:
        print("Cantidad inválida.")
        continue

    actualizar_stock(codigo, cantidad)

elif opcion == "5":
    print("Sistema finalizado.")
    break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    inicializar_base_datos()
    mostrar_menu()

    def buscar_producto(codigo):
    """Busca un producto registrado por su código."""
    with obtener_conexion() as conexion:
    conexion.execute(
        """
        INSERT INTO productos (codigo, nombre, categoria, precio, stock)
        VALUES (?, ?, ?, ?, ?)
        """,
        (codigo, nombre, categoria, precio, stock),
    )

print("Producto registrado correctamente.")


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "jugueteria.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def obtener_conexion():
    """Crea una conexión con la base de datos SQLite."""
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion


def inicializar_base_datos():
    """Crea las tablas del sistema si todavía no existen."""
    with obtener_conexion() as conexion:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as archivo:
            conexion.executescript(archivo.read())

def actualizar_stock(codigo, cantidad):
    """Modifica el stock de un producto."""
    producto = buscar_producto(codigo)

    if producto is None:
        print("Error: producto no encontrado.")
        return False

    nuevo_stock = producto["stock"] + cantidad

    if nuevo_stock < 0:
        print("Error: stock insuficiente.")
        return False

    with obtener_conexion() as conexion:
        conexion.execute(
            "UPDATE productos SET stock = ? WHERE codigo = ?",
            (nuevo_stock, codigo),
        )

    print(f"Stock actualizado. Nuevo stock: {nuevo_stock}")
    return True

def crear_venta():
    """Crea una nueva venta vacía y devuelve su identificador."""
    fecha = datetime.now().isoformat(timespec="seconds")

    with obtener_conexion() as conexion:
        cursor = conexion.execute(
            "INSERT INTO ventas (fecha, total) VALUES (?, ?)",
            (fecha, 0),
        )

        return cursor.lastrowid