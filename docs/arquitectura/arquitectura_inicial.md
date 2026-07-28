# Arquitectura Inicial del Sistema

## 1. Proyecto

Sistema de Gestión de Ventas para Mini Juguetería.

## 2. Objetivo

Definir la arquitectura inicial del sistema para organizar los componentes
relacionados con productos, ventas, inventario y almacenamiento de datos.

## 3. Arquitectura propuesta

Para esta primera versión se utilizará una arquitectura simple organizada
en tres componentes principales:

1. Interfaz de usuario.
2. Lógica del sistema.
3. Base de datos.

## 4. Componentes

### 4.1 Interfaz de usuario

Permitirá al usuario interactuar con las funciones principales del sistema.

Funciones:

- Registrar productos.
- Consultar productos.
- Registrar ventas.
- Consultar stock.
- Visualizar totales.

### 4.2 Lógica del sistema

Contendrá las reglas principales del negocio.

Responsabilidades:

- Validar información de productos.
- Registrar ventas.
- Calcular subtotales y totales.
- Actualizar el inventario.
- Evitar ventas con stock insuficiente.

### 4.3 Base de datos

Permitirá almacenar la información del sistema.

Principales entidades:

- Producto.
- Venta.
- DetalleVenta.

## 5. Flujo general

Usuario  
↓  
Interfaz del sistema  
↓  
Lógica de negocio  
↓  
Base de datos

## 6. Módulos principales

### Módulo de productos

Permite registrar y consultar juguetes.

### Módulo de ventas

Permite registrar ventas de uno o varios productos.

### Módulo de inventario

Controla el stock disponible y actualiza las cantidades después de una venta.

## 7. Tecnologías para la simulación

- Python para el código principal.
- SQLite como referencia para almacenamiento de datos.
- Git para control de versiones.
- Markdown para documentación.

## 8. Estado

Versión: 1.0  
Estado: Aprobado  
Línea base: LB-001