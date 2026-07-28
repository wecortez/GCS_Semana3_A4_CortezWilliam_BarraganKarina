# Plan de Gestión de Configuración del Software

## 1. Información general

**Proyecto:** Sistema de Gestión de Ventas para Mini Juguetería  
**Versión del plan:** 1.0  
**Línea base inicial:** LB-001  
**Integrantes:**
- William Cortez
- Karina Barragán

## 2. Objetivo

Definir las actividades básicas de Gestión de Configuración del Software
para controlar los elementos del proyecto, mantener la trazabilidad de los
cambios y asegurar que el equipo trabaje sobre versiones identificadas y
controladas.

## 3. Elementos de configuración

Los principales elementos de configuración del proyecto son:

- Requerimientos del sistema.
- Arquitectura del sistema.
- Código fuente.
- Archivos de configuración.
- Esquema de base de datos.
- Casos de prueba.
- Plan de Gestión de Configuración.
- Plan de calidad.
- Manual de usuario.
- Historial de cambios.
- Documentación general del proyecto.

El inventario detallado se encuentra en:

`INVENTARIO_CONFIGURACION.md`

## 4. Repositorio

El proyecto será administrado mediante Git.

La rama principal será:

`main`

La rama `main` contendrá versiones revisadas y estables del proyecto.

Los integrantes podrán crear ramas individuales para realizar cambios
sin modificar directamente la versión estable.

Ejemplos:

- `feature/productos`
- `feature/ventas`
- `feature/inventario`

## 5. Control de versiones

Los cambios serán registrados mediante commits descriptivos.

Ejemplos:

`Agregar requerimientos iniciales del sistema`

`Implementar registro de productos`

`Actualizar esquema de base de datos`

Las líneas base serán identificadas mediante tags.

Ejemplo:

`LB-001`

## 6. Línea base inicial

La primera línea base del proyecto será:

**LB-001**

Representará la versión inicial revisada del proyecto y contendrá los
elementos de configuración aprobados para la versión 1.0.

Su descripción se encuentra en:

`docs/lineas_base/LB-001.md`

## 7. Control de cambios

Los cambios posteriores a la línea base deberán seguir el siguiente proceso:

1. Identificar el cambio requerido.
2. Registrar el cambio.
3. Crear una rama de trabajo.
4. Realizar la modificación.
5. Verificar que el cambio funcione correctamente.
6. Integrar el cambio en la rama principal.
7. Registrar el cambio en `CHANGELOG.md`.

## 8. Responsabilidades

### William Cortez

Responsable principalmente de:

- Requerimientos.
- Código fuente.
- Casos de prueba.
- Plan de Gestión de Configuración.

### Karina Barragán

Responsable principalmente de:

- Arquitectura.
- Configuración.
- Base de datos.
- Plan de calidad.
- Manual de usuario.

### Ambos integrantes

Responsables de:

- README.
- CHANGELOG.
- Revisión de líneas base.
- Aprobación de cambios importantes.

## 9. Estados de los elementos

Los elementos podrán tener los siguientes estados:

- En desarrollo.
- Revisado.
- Aprobado.
- Estable.
- Activo.

## 10. Criterio de aprobación de LB-001

La línea base LB-001 será aprobada cuando:

- Los requerimientos estén definidos.
- La arquitectura inicial esté documentada.
- El código inicial sea funcional.
- El esquema de base de datos esté definido.
- Los casos de prueba estén documentados.
- Los archivos de configuración estén disponibles.
- Los documentos principales hayan sido revisados.