# 02 — Lista de pruebas web (Test List)

Las pruebas se ejecutan mediante el cliente de pruebas de Django contra las
vistas HTTP. Cada escenario recorre pasos del usuario; no se prueban funciones
internas como sustituto de la interfaz web.

| ID | Escenario | Regla | Resultado esperado | Test |
|---|---|---|---|---|
| W1 | Abrir la página principal | — | Se muestra acceso a comprar entradas | `test_inicio_web_muestra_acceso_a_compra_de_entradas` |
| W2 | Usuario anónimo intenta comprar | R1 | Redirección al inicio de sesión | `test_visitante_sin_registro_no_puede_iniciar_una_compra` |
| W3 | Registrarse, iniciar sesión y comprar en efectivo | R1–R8 | Confirmación con fecha y cantidad y email enviado | `test_compra_en_efectivo_confirma_fecha_cantidad_y_envia_email` |
| W4 | Comprar pases regular y VIP | R4–R5 | Total calculado con los precios configurados | `test_compra_calcula_total_segun_pase_de_cada_visitante` |
| W5 | Comprar con tarjeta | R6–R7 | Redirección a Mercado Pago | `test_compra_con_tarjeta_redirige_a_mercado_pago` |
| W6 | Omitir el medio de pago | R6 | Error visible y sin email de confirmación | `test_compra_sin_medio_de_pago_muestra_error_y_no_envia_email` |
| W7 | Seleccionar una fecha pasada | R2 | Error visible y compra no confirmada | `test_compra_rechaza_fecha_anterior_a_hoy` |
| W8 | Solicitar 11 entradas | R3 | Rechazo del límite máximo de 10 | `test_compra_rechaza_mas_de_diez_entradas` |
| W9 | Omitir edad o tipo de pase | R4 | Errores de validación visibles | `test_compra_rechaza_edad_o_tipo_de_pase_faltante` |

## Datos de prueba

- Cada escenario crea su propio cliente y usa SQLite en memoria.
- Los precios predeterminados de pruebas son 1000 para pase regular y 2000 para
  VIP; se sobreescriben en el escenario de cálculo.
- El envío de correo usa el backend local de Django, sin servicios externos.
- La URL de Mercado Pago en pruebas usa el dominio reservado `mercadopago.test`.

## Estado de la etapa RED

Las pruebas describen rutas HTTP todavía no implementadas y deben fallar hasta
que se complete GREEN. No se consideran válidas como RED fallas de importación,
configuración o dependencias; el resultado esperado es un rechazo HTTP por rutas
aún no conectadas.
