# 01 — Concepto de la US

## User Story

> **Comprar entradas**
> COMO visitante registrado QUIERO comprar entradas indicando fecha, cantidad,
> edad de cada visitante y tipo de pase PARA asegurar mi visita al parque.

## Criterios de aceptación y reglas

| # | Regla |
|---|---|
| R1 | Solo usuarios registrados e iniciados pueden comprar entradas. |
| R2 | Se elige una fecha desde hoy hasta un mes de anticipación. El parque cierra los lunes, el 25 de diciembre y el 1 de enero. |
| R3 | Se pueden comprar hasta 10 entradas por usuario y fecha, acumuladas entre transacciones. |
| R4 | Para cada entrada se indica la edad y el tipo de pase (común o VIP). Hasta 3 años no paga; de 4 a 15 y desde los 60 años obtiene 50% de descuento. |
| R5 | Se muestra el monto total calculado por tipo de pase y descuento por edad. Los precios son $10.000 para común y $20.000 para VIP. |
| R6 | Se elige un medio de pago: efectivo en boletería o tarjeta. |
| R7 | La tarjeta se prueba con una pantalla local simulada de Mercado Pago; el efectivo se completa en boletería. |
| R8 | La compra informa cantidad, fecha y total y muestra un modal de correo de confirmación simulado. No se envían mensajes desde el flujo de compra. |
| R9 | La compra para el mismo día se permite hasta las 17:30 inclusive. |

## Supuestos acordados

- Los precios por defecto son $10.000 para común y $20.000 para VIP; pueden
  ajustarse por configuración.
- Las fechas pasadas, los lunes, el 25/12 y el 1/1 no se pueden comprar. El
  calendario limita el horizonte a un mes y el servidor vuelve a validar todas
  las reglas.
- Los descuentos por edad se aplican por visitante antes de sumar el total.
- El flujo de tarjeta y la confirmación de correo son simulaciones locales de
  desarrollo; no se realizan cobros ni se envían correos al comprar.
- El usuario se identifica con email y contraseña.
- Los datos de visitantes y la compra confirmada quedan asociados a la compra para
  presentar la información necesaria al ingreso.

## Fuera de alcance inicial

- Administración de precios y calendario desde una interfaz.
- Procesamiento real de tarjetas, credenciales de producción y confirmación
  asíncrona de Mercado Pago o envío de correos desde la compra.
- Emisión de comprobantes fiscales.
