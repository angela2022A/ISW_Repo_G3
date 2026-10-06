# 04 — Decisiones de diseño

> Las decisiones marcadas como *iniciales* se tomaron antes del primer ciclo para que los tests compilen.
> Las marcadas *(completar)* se documentan a medida que emergen de los ciclos TDD.

## Decisiones iniciales

### D-01. Lenguaje y framework: Python + pytest
- pytest permite tests como funciones simples con `assert`, *fixtures* para datos compartidos y `parametrize` para varias clases de equivalencia en un solo test.
- Estilo de código: PEP 8 (líneas ≤ 79 caracteres, `snake_case`, nombres descriptivos en español). *(Ajustar si la guía de estilo del TP2 indica otra cosa.)*

### D-02. La US se expone como `ServicioInscripcion.inscribir_actividad(...)`
- Sigue el formato de la cátedra: los pasos del caso de prueba "llaman a la US" con los parámetros que ingresa el visitante.
- Las dependencias (parque, notificador, generador de QR) se reciben en el constructor y no como parámetros de la US: la llamada queda igual a lo que el visitante ingresa.

### D-03. Cada rechazo es una excepción específica
- Una excepción por regla violada (`SinCupoError`, `TallaRequeridaError`, etc.), todas heredan de `InscripcionError`.
- Los tests las verifican con `pytest.raises`. El nombre de la excepción documenta qué regla se rompió.

### D-04. Dobles de prueba para email y QR (inyección de dependencias)
- Un test unitario debe ser aislado, rápido y repetible: no puede enviar mails reales.
- **Mock** del notificador: permite verificar *si* se envió el email y *con qué* inscripción (U1, D8).
- **Stub** del generador de QR: devuelve siempre `QR-FAKE-123`.
- Se aplica el principio de inversión de dependencias (SOLID): el servicio depende de "algo que sepa enviar" y no de un servidor de mail concreto.
- Ref.: Blé, *Diseño Ágil con TDD*, cap. 6 (Mocks y otros dobles de prueba) y cap. 7 (S.O.L.I.D.).

### D-05. Aislamiento entre tests
- La fixture `parque` crea una copia profunda del catálogo en cada test, así ningún test depende de los cupos que consumió otro (patrón *Isolated Test*).

### D-06. Visitantes como diccionarios
- Se modelan como lo que ingresa el visitante en el formulario. Si durante el refactor aparece lógica propia del visitante, se evaluará extraer una clase `Visitante`.

## Decisiones que emergen de los ciclos *(completar)*

| Ciclo | Decisión / refactor | Motivo |
|---|---|---|
| | | |

## Pseudocódigo de la US

*(Completar al final: versión antes y después del refactor, con un bloque `# Caso de prueba ...` por cada prueba de usuario, como en el ejemplo Taxi Mobile de la cátedra.)*
