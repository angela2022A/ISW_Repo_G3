# 02 — Lista de pruebas web (Test List)

Las pruebas se ejecutan mediante el cliente de pruebas de Django contra las
vistas HTTP. Cada escenario recorre pasos del usuario; no se prueban funciones
internas como sustituto de la interfaz web.

| ID | Escenario | Regla | Resultado esperado | Test |
|---|---|---|---|---|
| W1 | Abrir la página principal | — | Se muestra acceso a comprar entradas | `test_inicio_web_muestra_acceso_a_compra_de_entradas` |
| W2 | Usuario anónimo intenta comprar | R1 | Redirección al inicio de sesión | `test_visitante_sin_registro_no_puede_iniciar_una_compra` |
| W3 | Registrarse, iniciar sesión y comprar en efectivo | R1–R8 | Confirmación con fecha y cantidad; mensaje de correo simulado, sin envío real | `test_compra_en_efectivo_envia_mail_de_confirmacion_al_usuario` |
| W4 | Comprar pases regular y VIP | R4–R5 | Total calculado con los precios configurados | `test_compra_calcula_total_segun_pase_de_cada_visitante` |
| W5 | Comprar con tarjeta | R6–R7 | Redirección a Mercado Pago | `test_compra_con_tarjeta_redirige_a_mercado_pago` |
| W6 | Omitir el medio de pago | R6 | Error visible y sin email de confirmación | `test_compra_sin_medio_de_pago_muestra_error_y_no_envia_email` |
| W7 | Seleccionar una fecha pasada | R2 | Error visible y compra no confirmada | `test_compra_rechaza_fecha_anterior_a_hoy` |
| W8 | Solicitar 11 entradas | R3 | Rechazo del límite máximo de 10 | `test_compra_rechaza_mas_de_diez_entradas` |
| W9 | Omitir edad o tipo de pase | R4 | Errores de validación visibles | `test_compra_rechaza_edad_o_tipo_de_pase_faltante` |
| W10 | Ver el formulario de compra | — | Forma de pago en sección aparte de los visitantes | `test_formulario_separa_forma_de_pago_de_datos_de_visitantes` |
| W11 | Elegir sábado o domingo | R2 | Rechazo con mensaje de apertura de lunes a viernes | `test_compra_rechaza_fines_de_semana` |
| W12 | Crear y usar la cuenta compartida | R1 | Permite iniciar sesión, comprar y cerrar sesión | `test_cuenta_compartida_permite_iniciar_sesion_y_cerrar_sesion` |
| W13 | Ingresar letras en campos numéricos | R3–R4 | Se quitan en el navegador y el servidor rechaza datos inválidos | `test_compra_rechaza_letras_en_campos_numericos` |
| W14 | Ver el formato de fecha y campos numéricos | — | Calendario nativo en región argentina, fecha día/mes/año y teclado numérico | `test_formulario_muestra_fecha_dia_mes_anio_y_campos_solo_numericos` |

## Datos de prueba

- Cada escenario crea su propio cliente y usa SQLite en memoria.
- Los precios predeterminados de pruebas son 1000 para pase regular y 2000 para
  VIP; se sobreescriben en el escenario de cálculo.
- Las compras no envían correo por ahora; la pantalla muestra el mensaje
  «Mail enviado (simulado)».
- La URL de Mercado Pago en pruebas usa el dominio reservado `mercadopago.test`.
- Las fechas de compra exitosas se generan para un día hábil futuro; las pruebas
  parametrizan ambos días del fin de semana para comprobar el rechazo.
  - El calendario usa `type="date"` con idioma regional `es-AR`, para presentar
    la fecha como `dd/mm/aaaa`; el navegador envía el valor interno ISO
    `aaaa-mm-dd` al servidor.

## Resultado de los ciclos

En RED, las nueve pruebas originales fallaron porque las rutas HTTP aún no
estaban implementadas (HTTP 404). Después de implementar GREEN, esas nueve
pruebas pasaron contra la aplicación web. Tras las mejoras posteriores se
amplió la suite a 12 casos: **12 aprobados, 0 fallidos**, incluyendo separación
de la forma de pago y rechazo de sábado y domingo. No se consideran válidas como
RED fallas de importación, configuración o dependencias.
