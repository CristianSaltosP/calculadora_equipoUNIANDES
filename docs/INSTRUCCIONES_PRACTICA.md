# Instrucciones Paso a Paso (para Docente y Estudiantes)

## Roles
- **Gestor de Configuración**: versiones, ramas, tags, releases, control de cambios.
- **Desarrollador**: implementa código y pruebas.
- **Auditor**: verifica documentación, auditoría y cumplimiento.
- **Cliente**: propone cambios (lo representa el docente).

## Preparación (Docente)
1. Cree/duplique un repo en GitHub (público para la clase).
2. Suba el contenido de esta carpeta o suba el ZIP directamente a GitHub.
3. Abra **Issues** predefinidos:
   - `REQ-1: Funciones básicas de calculadora`
   - `CR-1: Agregar mediana y desviación estándar`
   - `DOC-1: Completar CI, Auditoría e ISO`
4. Asigne roles en cada equipo.

## Sesión (90–110 min)

### 1) Identificación de Configuración (10–15 min)
- Completen `templates/CONFIG_ITEMS.csv` con: nombre CI, versión inicial `v1.0.0`, responsable, ubicación (ruta).
- Confirmen que `src/`, `tests/` y `templates/` están versionados.

### 2) Línea Base 1 (10 min)
**GitHub (web):**
- `Code → Add file → Upload files` y suban todo.
- `Releases → Draft a new release → Tag: v1.0.0 → Release title: Línea Base 1` y publicar.

(**CLI opcional**)
```
git tag v1.0.0
git push origin v1.0.0
```

### 3) Control de Cambios (25–30 min)
- El docente actúa como **Cliente** y solicita:
  - **CR-1**: agregar funciones `mediana` y `desviacion_estandar` en `calculadora.py` y pruebas.
- Registrar la solicitud en `templates/CHANGE_REQUEST.md`.
- Reunir al **CAB** (equipo) y decidir: aprobado/rechazado (se espera *aprobado*).
- Crear rama `feature/estadistica`.
- Implementar el cambio y actualizar versión a `v1.1.0` en README del código.
- Abrir **Pull Request** a `main`. El **Auditor** revisa:
  - PR vinculado a Issue `CR-1`.
  - Pasan pruebas de `tests/test_calculadora.py` (ampliadas).
  - Actualizados `AUDIT_LOG.csv` y `CONFIG_ITEMS.csv` si cambió algo.

(**CLI opcional**)
```
git checkout -b feature/estadistica
# editar archivos
git add .
git commit -m "CR-1: agrega mediana y desviacion_estandar con pruebas"
git push -u origin feature/estadistica
# abrir PR en GitHub
```

### 4) Auditoría y Calidad (20–25 min)
- Completen `templates/AUDIT_LOG.csv` (quién, qué, cuándo, por qué).
- Llenen `templates/ISO25010_CHECKLIST.csv` (1–5) para: Mantenibilidad, Seguridad, Usabilidad, Portabilidad, Eficiencia.
- Escriban conclusiones (3–5 líneas) al final de la checklist.

### 5) Línea Base 2 (5–10 min)
- Una vez mergeado el PR, crear **Release v1.1.0** (Línea Base 2).
- Comparar `v1.0.0` vs `v1.1.0` en GitHub: `Compare` para ver diferencias.

## Rubrica Sugerida (100 pts)
- CI identificados y actualizados (15)
- Línea Base 1 creada (10)
- Control de cambios (CAB, PR, vínculo a Issue) (20)
- Pruebas unitarias pasan (15)
- Auditoría (LOG completo y evidencias) (15)
- Checklist ISO/IEC 25010 y mejoras propuestas (15)
- Presentación breve (5)

## Evidencias
- Capturas de: Releases (tags), PR mergeado, Issues, Diff entre versiones, hoja de auditoría, checklist ISO.

