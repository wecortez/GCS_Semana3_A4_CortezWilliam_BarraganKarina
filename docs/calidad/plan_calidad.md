# Plan de Calidad

## 1. Proyecto

Sistema de Gestión de Ventas para Mini Juguetería.

## 2. Objetivo

Definir criterios básicos de calidad que permitan verificar que el sistema
cumpla los requerimientos establecidos y que sus elementos de configuración
se mantengan controlados y trazables.

## 3. Criterios de calidad

### Funcionalidad

El sistema debe permitir:

- Registrar productos.
- Consultar productos.
- Registrar ventas.
- Actualizar el inventario.
- Calcular el total de una venta.

### Confiabilidad

El sistema debe evitar operaciones incorrectas, como vender una cantidad
superior al stock disponible.

### Usabilidad

Las opciones principales deben ser fáciles de identificar y utilizar.

### Mantenibilidad

El código debe mantenerse organizado y con nombres comprensibles.

### Trazabilidad

Los cambios realizados deberán quedar registrados mediante Git y
documentados cuando correspondan en `CHANGELOG.md`.

## 4. Verificación

Se realizarán casos de prueba para comprobar:

- Registro correcto de productos.
- Consulta de productos.
- Registro de ventas.
- Actualización del stock.
- Cálculo correcto del total.
- Validación de stock insuficiente.

## 5. Control de calidad mediante GCS

Para apoyar la calidad del proyecto se utilizarán:

- Control de versiones con Git.
- Identificación de elementos de configuración.
- Línea base LB-001.
- Historial de cambios.
- Casos de prueba.
- Responsables definidos para cada elemento.

## 6. Criterio de aceptación

Una funcionalidad será considerada aceptada cuando:

1. Cumpla el requerimiento asociado.
2. No genere errores durante la prueba.
3. Mantenga consistencia con la base de datos.
4. El cambio quede registrado en Git.

## 7. Estado

Versión: 1.0  
Estado: Revisado  
Línea base: LB-001

## Matriz básica de trazabilidad

| Requerimiento | Funcionalidad | Caso de prueba |
|---|---|---|
| RF-001 | Registrar producto | CP-001, CP-003, CP-006 |
| RF-002 | Registrar venta | CP-010, CP-012 |
| RF-003 | Actualizar inventario | CP-008, CP-009, CP-010, CP-011 |
| RF-004 | Consultar productos | CP-002 |
| RF-005 | Calcular total | CP-005, CP-010 |