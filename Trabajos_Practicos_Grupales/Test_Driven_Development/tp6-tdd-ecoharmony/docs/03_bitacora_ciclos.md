# 03 — Bitácora de ciclos Red-Green-Refactor

Se trabaja en el orden TDD **RED → GREEN → REFACTOR** y se pausa al final de
cada fase para que el grupo haga su push antes de continuar.

| Ciclo | Pruebas | RED | GREEN | REFACTOR | Push del grupo |
|---|---|---|---|---|---|
| 1 | W1–W9: compra de entradas vía web | 9 pruebas fallan: las rutas todavía no están conectadas (HTTP 404) | Pendiente | Pendiente | Esperando push del grupo |

En RED, las fallas deben provenir de las rutas aún no implementadas. En GREEN se
implementa lo mínimo para pasar las pruebas. En REFACTOR se mejora el diseño,
conservando todos los resultados y volviendo a ejecutar la suite completa.
