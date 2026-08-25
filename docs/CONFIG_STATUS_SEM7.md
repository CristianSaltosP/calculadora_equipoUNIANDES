# INFORME DE ESTADO DE CONFIGURACIÓN

## Semana 7 - Gestión de la Configuración del Software

**Fecha de revisión:** 24/08/2026

### 1. Baseline / Release

Baseline vigente: v1.0.0

Nueva configuración: candidata a v1.1.0

Estado: pendiente de creación de Tag y Release.

### 2. Versión / Tag

Tag vigente: v1.0.0

Nueva versión propuesta: v1.1.0

Commit / referencia actual: d1b68ca

### 3. Cambios aprobados

- CR-1: incorporación de mediana y desviación estándar.
  Evidencia: feature/estadistica, pruebas unitarias y Merge CR-1.

- CR-2: incorporación de función potencia.
  Evidencia: feature/potencia, commit 3bcceed, Merge CR-2 04673a9 y auditoría d1b68ca.

### 4. Elementos de Configuración afectados

1. src/calculadora.py
2. tests/test_calculadora.py
3. docs/CR-2_potencia.md

### 5. Problema frecuente detectado

Divergencia de una rama de desarrollo respecto de la rama principal main durante la implementación del CR-2.

### 6. Acción de mejora aplicada

Se actualizó feature/potencia mediante rebase sobre main, se ejecutaron nuevamente las pruebas unitarias y posteriormente se realizó la integración controlada mediante merge.