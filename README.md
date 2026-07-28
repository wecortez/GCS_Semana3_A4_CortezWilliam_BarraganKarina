# Sistema de Gestión de Ventas para Mini Juguetería

Proyecto académico desarrollado para la asignatura
**Gestión de la Configuración del Software**.

## Integrantes

- William Cortez
- Karina Barragán

## Descripción

El proyecto consiste en un sistema básico de gestión de ventas para una
mini juguetería.

Permitirá gestionar productos, inventario y ventas, manteniendo controlados
los principales artefactos mediante prácticas de Gestión de Configuración
del Software.

## Funcionalidades principales

- Registrar productos.
- Consultar productos.
- Registrar ventas.
- Actualizar inventario.
- Calcular totales de venta.

## Estructura del repositorio

```text
config/
├── CM_PLAN.md
└── config.example.json

database/
└── schema.sql

docs/
├── arquitectura/
│   └── arquitectura_inicial.md
├── calidad/
│   └── plan_calidad.md
├── lineas_base/
│   └── LB-001.md
├── manuales/
│   └── manual_usuario.md
└── requerimientos/
    └── requerimientos_v1.md

src/
└── app.py

tests/
└── casos_prueba.md

CHANGELOG.md
INVENTARIO_CONFIGURACION.md
README.md