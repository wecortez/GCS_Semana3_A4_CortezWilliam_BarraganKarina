# Simulación de Cambio y su Impacto por Fase

## 1. Proyecto

Sistema de Gestión de Ventas para Mini Juguetería.

## 2. Cambio seleccionado

Se selecciona un cambio relacionado con el rendimiento del sistema.

**RNF-001:** El sistema debe completar la búsqueda de productos por código
en un tiempo menor o igual a 2 segundos en al menos el 95% de las
ejecuciones de prueba.

Este cambio requiere analizar diferentes fases del ciclo de desarrollo,
debido a que afecta requisitos, diseño, implementación, base de datos,
pruebas y documentación.

## 3. Análisis de impacto por fase

| Fase | ¿Qué cambia? | EC afectados | Riesgo si no se controla | Evidencia de validación |
|---|---|---|---|---|
| Requisitos | Se incorpora el RNF-001 y su criterio de aceptación de búsqueda ≤ 2 segundos en al menos el 95% de las pruebas. | EC-001 | El requisito puede quedar ambiguo o no ser considerado durante el desarrollo. | Revisión del archivo de requerimientos y commit del cambio. |
| Diseño | Se revisa la arquitectura para identificar los componentes involucrados en la búsqueda de productos. | EC-002 | La solución diseñada podría no considerar el rendimiento requerido. | Actualización y revisión de la arquitectura del sistema. |
| Implementación | Se revisa y optimiza la función encargada de buscar productos por código. | EC-003 | La búsqueda podría superar el tiempo establecido o introducir errores funcionales. | Revisión del código y commit de implementación. |
| Base de datos | Se revisa la consulta utilizada para localizar productos y la estructura de la tabla de productos. | EC-005 | Una consulta ineficiente podría aumentar el tiempo de respuesta al crecer la cantidad de registros. | Revisión del esquema y ejecución de consultas de prueba. |
| Pruebas | Se incorpora una prueba para medir el tiempo de respuesta de la búsqueda de productos. | EC-006 | No existiría evidencia objetiva para demostrar el cumplimiento del RNF-001. | Resultado de prueba con búsqueda ≤ 2 segundos. |
| Documentación y control | Se registra el cambio, los EC afectados y la evidencia generada. | EC-007, EC-010 | Se perdería trazabilidad sobre qué cambió, por qué cambió y cómo fue validado. | CHANGELOG, documentación actualizada y commit del cambio. |

## 4. Elementos de configuración afectados

El cambio afecta los siguientes elementos de configuración:

- EC-001 Requerimientos del sistema.
- EC-002 Arquitectura del sistema.
- EC-003 Código fuente principal.
- EC-005 Esquema de base de datos.
- EC-006 Casos de prueba.
- EC-007 Plan de Gestión de Configuración.
- EC-010 Historial de cambios.

## 5. Trazabilidad del cambio

La relación entre el cambio y los elementos afectados se representa de la
siguiente manera:

RNF-001
→ Requerimientos
→ Arquitectura
→ Código fuente
→ Base de datos
→ Casos de prueba
→ Evidencia de validación
→ Historial de cambios

Esta relación permite identificar qué elementos fueron modificados y qué
evidencia demuestra que el cambio fue implementado correctamente.

## 6. Riesgo del cambio sin control

Si el cambio se realizara únicamente en el código fuente sin actualizar
los demás elementos relacionados, se perdería la trazabilidad del proyecto.

Por ejemplo, podría existir una optimización en el código sin que el
requerimiento estuviera documentado o sin una prueba que permita verificar
si realmente se cumple el tiempo de respuesta establecido.

La Gestión de Configuración permite controlar estas modificaciones y
mantener consistencia entre los diferentes elementos del proyecto.

## 7. Evidencia de validación

Para validar el cambio se utilizarán las siguientes evidencias:

- Actualización del requerimiento RNF-001.
- Revisión de la arquitectura.
- Modificación controlada del código fuente.
- Revisión de la consulta a la base de datos.
- Caso de prueba de rendimiento.
- Commit correspondiente al cambio.
- Registro del cambio en `CHANGELOG.md`.

## 8. Estado

Versión: 1.0  
Estado: Aprobado  
Cambio analizado: RNF-001 Rendimiento de búsqueda