# 03 — Bitácora de ciclos Red-Green-Refactor

Completar una fila por ciclo **mientras se trabaja**, no al final. Hacer un commit por fase:
`RED: <test>` → `GREEN: <test>` → `REFACTOR: <qué se mejoró>` (si hubo refactor).

Para correr solo el test del ciclo: `pytest -k <nombre_del_test>`.

| Ciclo | Test (ID) | RED: ¿falló por el motivo correcto? | GREEN: patrón usado (Fake It / Triangulación / Obvious Implementation) | REFACTOR: qué se mejoró | Commits |
|---|---|---|---|---|---|
| 1 | U1 parte 1 — inscripción válida (*Starter Test*) | | | | |
| 2 | D1 — actividad fuera del listado | | | | |
| 3 | U5 — sin T&C | | | | |
| 4 | D4 — cero personas | | | | |
| 5 | D5 — cantidad ≠ visitantes | | | | |
| 6 | D6 — visitante incompleto | | | | |
| 7 | U6 — talla requerida | | | | |
| 8 | U3 — talla no requerida | | | | |
| 9 | U4 — horario no disponible | | | | |
| 10 | U2 — sin cupo | | | | |
| 11 | D2 / D3 — límites de cupo | | | | |
| 12 | D7 — descuento de cupos | | | | |
| 13 | U1 parte 2 — email con QR | | | | |
| 14 | D8 — rechazo sin email | | | | |

## Orientación sobre los patrones esperados

- **Ciclo 1:** *Fake It* — devolver una `Inscripcion` armada con los parámetros recibidos, sin validar nada.
- **Ciclo 2:** *Triangulación* — el segundo test obliga a dejar de aceptar cualquier actividad y consultar el catálogo del parque.
- **Ciclos 3 a 7:** validaciones simples, probablemente *Obvious Implementation*.
- **Ciclo 8:** puede pasar sin tocar código si el ciclo 7 consultó `requiere_talla`. Anotarlo igual: es un test que confirma el diseño.
- **Ciclos 10 a 12:** aparece la lógica de cupo; candidato a refactor que mueva la lógica a `Parque`.
- **Ciclo 13:** uso de los dobles de prueba (stub del QR, mock del notificador).
- **Refactor final:** la función tiende a quedar larga (un `if` por regla); extraer métodos como `_validar_visitantes()` o `_validar_cupo()`.
