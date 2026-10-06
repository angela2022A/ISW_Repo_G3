# TP6 — TDD: Inscribirme a actividad (EcoHarmony Park)

Implementación de la US **"Inscribirme a actividad"** aplicando TDD (Red-Green-Refactor) en Python + pytest.

## Estructura

```
tp6-tdd-ecoharmony/
├── src/ecoharmony/
│   ├── inscripcion.py      ← US: ServicioInscripcion.inscribir_actividad(...)
│   ├── parque.py           ← catálogo de actividades, horarios y cupos
│   └── errores.py          ← una excepción por motivo de rechazo
├── tests/
│   ├── conftest.py         ← datos de prueba + dobles (mock/stub)
│   └── test_inscripcion.py ← lista de pruebas, en orden de ciclo
└── docs/
    ├── 01_concepto.md            ← reglas, supuestos, alcance
    ├── 02_lista_de_pruebas.md    ← trazabilidad US → tests
    ├── 03_bitacora_ciclos.md     ← registro de cada ciclo R-G-R
    └── 04_decisiones_de_diseno.md
```

## Puesta en marcha

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest                      # todos los tests
pytest -k sin_cupo          # un test puntual
```

En VS Code / Cursor: instalar la extensión **Python**, seleccionar el intérprete `.venv` y abrir la pestaña **Testing** (ícono de matraz).

## Estado inicial

Todos los tests están en **RED**: la US lanza `NotImplementedError`. El código de producción se escribe ciclo por ciclo siguiendo `docs/03_bitacora_ciclos.md`.
