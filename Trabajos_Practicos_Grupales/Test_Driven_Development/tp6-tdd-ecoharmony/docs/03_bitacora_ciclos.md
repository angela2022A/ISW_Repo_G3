# 03 — Bitácora de ciclos Red-Green-Refactor

Se trabaja en el orden TDD **RED → GREEN → REFACTOR** y se pausa al final de
cada fase para que el grupo haga su push antes de continuar.

| Ciclo | Pruebas | RED | GREEN | REFACTOR | Push del grupo |
|---|---|---|---|---|---|
| 1 | W1–W9: compra de entradas vía web | 9 pruebas fallaron porque las rutas todavía no estaban conectadas (HTTP 404) | 9 pruebas pasan con la aplicación web Django implementada | Validaciones de fecha, cantidad y visitante extraídas en funciones dedicadas; las 9 pruebas siguen pasando | Histórico |
| 2 | W1–W17: reglas del dominio aclaradas con PO | Se agregaron casos de fecha, horarios, descuentos, límite por persona y simulaciones | Se actualizaron reglas del servidor y formulario; checkout/mail simulados localmente | Se alinearon criterios, pruebas y documentación | Validado: suite completa aprobada |

El primer ciclo documenta el desarrollo inicial. En el ciclo de alineación con
PO se reemplazaron las reglas provisionales por días de cierre, precios y
descuentos acordados, límites de compra y simulaciones de pago/correo. La suite
actual se ejecuta con 30 pruebas aprobadas.
