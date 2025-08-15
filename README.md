# Práctica Guiada: GCS + Calidad con una Calculadora

Este repositorio acompaña la práctica de **Gestión de la Configuración del Software (GCS)** y **Modelos de Calidad** usando un mini–proyecto de calculadora.

## Objetivos
- Aplicar identificación de configuración, control de versiones, control de cambios y auditoría.
- Establecer y proteger **Líneas Base** por medio de tags/releases.
- Evaluar calidad con una checklist basada en **ISO/IEC 25010**.

## Estructura
```
docs/                  → guía de práctica e instrucciones paso a paso
src/calculadora.py     → código de la calculadora (v1.0.0)
tests/test_calculadora.py → pruebas unitarias básicas
templates/             → plantillas (CI, Solicitudes de Cambio, Auditoría, ISO 25010)
.gitignore
README.md
```

## Flujo sugerido
1. Completar `templates/CONFIG_ITEMS.csv` para identificar los CI.
2. Subir código inicial y crear **tag** `v1.0.0` (Línea Base 1).
3. Registrar cambios solicitados en `templates/CHANGE_REQUEST.md`.
4. Trabajar en una rama de feature, abrir **Pull Request** y pasar pruebas.
5. Registrar auditoría en `templates/AUDIT_LOG.csv`.
6. Evaluar calidad con `templates/ISO25010_CHECKLIST.csv`.
7. Crear **tag** `v1.1.0` y **Release**.

Más detalle en `docs/INSTRUCCIONES_PRACTICA.md`.
