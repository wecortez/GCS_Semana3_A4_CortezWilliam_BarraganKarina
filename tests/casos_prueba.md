# Casos de Prueba

## Proyecto

Sistema de Gestión de Ventas para Mini Juguetería.

Versión: 1.0  
Estado: Aprobado  
Línea base: LB-001

---

## CP-001 Registrar producto correctamente

**Requerimiento asociado:** RF-001

### Datos de entrada

- Código: JUG001
- Nombre: Carro de juguete
- Categoría: Vehículos
- Precio: 10.50
- Stock: 15

### Resultado esperado

El producto se registra correctamente en el sistema.

### Estado

Aprobado

---

## CP-002 Consultar productos

**Requerimiento asociado:** RF-004

### Precondición

Debe existir al menos un producto registrado.

### Acción

Seleccionar la opción de consultar productos.

### Resultado esperado

El sistema muestra:

- Código.
- Nombre.
- Categoría.
- Precio.
- Stock.

### Estado

Aprobado

---

## CP-003 Registrar precio negativo

**Requerimiento asociado:** RF-001

### Datos de entrada

- Código: JUG002
- Nombre: Pelota
- Categoría: Deportes
- Precio: -5
- Stock: 10

### Resultado esperado

El sistema rechaza el registro porque el precio no puede ser negativo.

### Estado

Aprobado

---

## CP-004 Registrar stock negativo

**Requerimiento asociado:** RF-001

### Datos de entrada

- Código: JUG003
- Nombre: Muñeca
- Categoría: Muñecas
- Precio: 20
- Stock: -2

### Resultado esperado

El sistema rechaza el registro porque el stock no puede ser negativo.

### Estado

Aprobado

---

## CP-005 Calcular total

**Requerimiento asociado:** RF-005

### Datos de entrada

Precio: 10.00  
Cantidad: 3

### Resultado esperado

Total:

30.00

### Estado

Aprobado

---

## Casos pendientes para siguientes versiones

Los siguientes casos se implementarán después de LB-001:

- Registro completo de una venta.
- Descuento automático del stock.
- Validación de stock insuficiente.
- Persistencia de productos en base de datos.

---

## CP-006 Registrar producto con código duplicado

**Requerimiento asociado:** RF-001

### Precondición

Existe un producto registrado con código `JUG001`.

### Datos de entrada

- Código: JUG001
- Nombre: Camión
- Categoría: Vehículos
- Precio: 15.00
- Stock: 5

### Resultado esperado

El sistema rechaza el registro e informa que ya existe
un producto con el mismo código.

### Estado

Aprobado

---

## CP-007 Validar campos obligatorios

**Requerimiento asociado:** RF-001

### Datos de entrada

Nombre vacío.

### Resultado esperado

El sistema rechaza el registro del producto.

### Estado

Aprobado

## CP-008 Actualizar stock correctamente

**Requerimiento asociado:** RF-003

### Precondición

Producto JUG001 con stock 10.

### Acción

Agregar 5 unidades.

### Resultado esperado

El stock final del producto es 15.

### Estado

Aprobado

---

## CP-009 Evitar stock negativo

**Requerimiento asociado:** RF-003

### Precondición

Producto JUG001 con stock 5.

### Acción

Intentar descontar 8 unidades.

### Resultado esperado

El sistema rechaza la operación por stock insuficiente.

### Estado

Aprobado

## CP-010 Registrar venta correctamente

**Requerimientos asociados:** RF-002, RF-003, RF-005

### Precondición

Existe el producto:

- Código: JUG001
- Precio: 10.00
- Stock: 10

### Datos de entrada

Cantidad: 3

### Resultado esperado

- La venta se registra.
- El total es 30.00.
- El stock pasa de 10 a 7.

### Estado

Aprobado

---

## CP-011 Venta con stock insuficiente

**Requerimiento asociado:** RF-003

### Precondición

Producto con stock 2.

### Datos de entrada

Cantidad solicitada: 5.

### Resultado esperado

El sistema rechaza la venta y conserva el stock existente.

### Estado

Aprobado

---

## CP-012 Cantidad de venta inválida

**Requerimiento asociado:** RF-002

### Datos de entrada

Cantidad: 0.

### Resultado esperado

El sistema rechaza la operación.

### Estado

Aprobado