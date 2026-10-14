# 01 — Concepto de la US

## User Story

> **Comprar entradas**
> COMO visitante registrado QUIERO comprar entradas indicando fecha, cantidad,
> edad de cada visitante y tipo de pase PARA asegurar mi visita al parque.

## Criterios de aceptación y reglas

| # | Regla |
|---|---|
| R1 | Solo usuarios registrados e iniciados pueden comprar entradas. |
| R2 | Se elige una fecha de visita de hoy en adelante, de lunes a viernes. |
| R3 | La cantidad está entre 1 y 10 entradas. |
| R4 | Para cada entrada se indica la edad y el tipo de pase (regular o VIP). |
| R5 | Se muestra el monto total calculado con el precio correspondiente a cada pase. |
| R6 | Se elige un medio de pago: efectivo en boletería o tarjeta. |
| R7 | El pago con tarjeta redirige a Mercado Pago; el de efectivo se completa en boletería. |
| R8 | La compra confirmada informa la cantidad y fecha y envía un email de confirmación. |

## Supuestos acordados

- Los precios regular y VIP son provisorios y se configuran fuera del código.
- La fecha de hoy es válida; las fechas pasadas no.
- El parque abre de lunes a viernes. El enunciado no define los días de
  apertura, por lo que es un supuesto del grupo.
- No se simula un cobro real ni se integra con credenciales de Mercado Pago en las
  pruebas. Se verifica la redirección usando una URL de prueba configurable.
- El usuario se identifica con email y contraseña.
- Los datos de visitantes y la compra confirmada quedan asociados a la compra para
  presentar la información necesaria al ingreso.

## Fuera de alcance inicial

- Administración de precios y calendario desde una interfaz.
- Procesamiento real de tarjetas, credenciales de producción y confirmación
  asíncrona de Mercado Pago.
- Emisión de comprobantes fiscales.
