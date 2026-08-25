# CHANGE REQUEST (CR)

- **ID**: CR-2
- **Título**: Agregar función potencia a la calculadora
- **Descripción**: Implementar la función `potencia(base, exponente)` en `src/calculadora.py`, incorporando su respectiva prueba unitaria.
- **Justificación**: Ampliar las capacidades funcionales de la calculadora y aplicar un ciclo controlado de cambio de configuración.
- **Impacto**: Código fuente y pruebas unitarias. No modifica las funciones existentes.
- **Riesgos**: Resultados incorrectos ante una implementación inadecuada o ausencia de pruebas.
- **Estado**: Aprobado
- **Rama asociada**: `feature/potencia`
- **Elemento de configuración afectado**: `src/calculadora.py`
- **Prueba esperada**: `potencia(2, 3) == 8`

## VERIFICACIÓN DEL CAMBIO

- **Commit CR-2 después del rebase**: `3bcceed`
- **Integración en main**: `04673a9` — Merge CR-2: integrar función potencia
- **Pruebas ejecutadas**: 6
- **Resultado**: 6 pruebas aprobadas
- **Estado final del cambio**: Implementado, verificado e integrado.
