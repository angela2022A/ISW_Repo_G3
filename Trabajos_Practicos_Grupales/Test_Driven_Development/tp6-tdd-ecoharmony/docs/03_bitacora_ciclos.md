# 03 — Bitácora de ciclos Red-Green-Refactor

Se trabaja en el orden TDD **RED → GREEN → REFACTOR** y se pausa al final de
cada fase para que el grupo haga su push antes de continuar.

| Ciclo | Pruebas | RED | GREEN | REFACTOR | Push del grupo |
|---|---|---|---|---|---|
| 1 | W1–W9: compra de entradas vía web | 9 pruebas fallaron porque las rutas todavía no estaban conectadas (HTTP 404) | 9 pruebas pasan con la aplicación web Django implementada | Validaciones de fecha, cantidad y visitante extraídas en funciones dedicadas; las 9 pruebas siguen pasando | Esperando push de REFACTOR |

En RED, las fallas provinieron de las rutas aún no implementadas. En GREEN se
implementó el flujo necesario para pasar las pruebas. En REFACTOR se separó la
validación en funciones pequeñas, conservando las reglas y los mensajes
observables por el usuario. La suite se volvió a ejecutar con resultado 9/9.
