# Modelo de Calidad del Software

## 1. Proyecto

Sistema de Gestión de Ventas para Mini Juguetería.

## 2. Modelo seleccionado

Para evaluar la calidad del sistema se utiliza como referencia
el modelo ISO/IEC 25010.

Este modelo permite analizar características de calidad del producto
software mediante atributos que pueden ser relacionados con métricas
verificables y evidencias dentro del repositorio.

## 3. Atributos de calidad seleccionados

Se seleccionan seis atributos de calidad relevantes para el sistema:

- Adecuación funcional.
- Fiabilidad.
- Usabilidad.
- Seguridad.
- Mantenibilidad.
- Eficiencia.

## 4. Tabla de atributos y métricas

| Atributo | Definición | Métrica verificable | EC que lo soporta |
|---|---|---|---|
| Adecuación funcional | Capacidad del sistema para cumplir las funciones especificadas. | El 100% de los requisitos funcionales implementados debe contar con al menos un caso de prueba asociado. | EC-001, EC-003, EC-006 |
| Fiabilidad | Capacidad del sistema para mantener un funcionamiento correcto durante las operaciones previstas. | El 100% de las ventas con stock suficiente debe registrarse correctamente sin producir valores negativos de inventario. | EC-003, EC-005, EC-006 |
| Usabilidad | Facilidad con la que el usuario puede comprender y utilizar las funciones del sistema. | El 100% de las operaciones principales debe mostrar mensajes comprensibles de éxito, error o validación. | EC-003, EC-009 |
| Seguridad | Protección de la información y configuración frente a exposición o acceso no autorizado. | Deben existir 0 credenciales, contraseñas o datos sensibles almacenados en texto plano dentro de los archivos versionados. | EC-003, EC-004 |
| Mantenibilidad | Facilidad para modificar, corregir y ampliar el sistema de manera controlada. | El 100% de los cambios funcionales debe quedar registrado mediante commits identificables y documentado cuando corresponda en `CHANGELOG.md`. | EC-003, EC-007, EC-010 |
| Eficiencia | Capacidad del sistema para ejecutar sus operaciones utilizando adecuadamente el tiempo y los recursos. | Las búsquedas de productos por código deben completarse en un tiempo menor o igual a 2 segundos en al menos el 95% de las ejecuciones de prueba. | EC-003, EC-005, EC-006 |

## 5. Métricas principales

### 5.1 Adecuación funcional

**Métrica:** El 100% de los requisitos funcionales implementados debe
contar con al menos un caso de prueba asociado.

### Justificación

Esta métrica permite verificar que cada funcionalidad desarrollada tenga
evidencia de validación y mantenga relación con los requerimientos del sistema.

### Evidencia

- EC-001 Requerimientos del sistema.
- EC-003 Código fuente principal.
- EC-006 Casos de prueba.

---

### 5.2 Fiabilidad

**Métrica:** El 100% de las ventas realizadas con stock suficiente debe
registrarse correctamente y ninguna operación debe generar un stock negativo.

### Justificación

El control del inventario es una función crítica para el sistema, ya que
una venta debe reflejar correctamente la cantidad disponible de productos.

### Evidencia

- EC-003 Código fuente principal.
- EC-005 Esquema de base de datos.
- EC-006 Casos de prueba.

## 6. Relación con la Gestión de Configuración

Las métricas definidas se apoyan en elementos de configuración controlados
dentro del repositorio.

Esto permite mantener trazabilidad entre:

- Requerimientos.
- Código fuente.
- Base de datos.
- Configuración.
- Casos de prueba.
- Historial de cambios.

De esta forma, la calidad puede ser evaluada mediante evidencia técnica
versionada y verificable.

## 7. Estado

Versión: 1.0  
Estado: Aprobado  
Referencia: ISO/IEC 25010