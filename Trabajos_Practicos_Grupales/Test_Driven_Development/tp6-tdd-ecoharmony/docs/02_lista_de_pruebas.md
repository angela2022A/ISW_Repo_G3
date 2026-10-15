# 02 — Lista de pruebas web (Test List)

Las pruebas se ejecutan mediante el cliente de pruebas de Django contra las
vistas HTTP. Cada escenario recorre pasos del usuario; no se prueban funciones
internas como sustituto de la interfaz web.

| ID | Escenario | Regla | Resultado esperado | Test |
|---|---|---|---|---|
| W1 | Abrir la página principal | — | Se muestra acceso a comprar entradas | `test_inicio_web_muestra_acceso_a_compra_de_entradas` |
| W2 | Usuario anónimo intenta comprar | R1 | Redirección al inicio de sesión | `test_visitante_sin_registro_no_puede_iniciar_una_compra` |
| W3 | Registrarse, iniciar sesión y comprar en efectivo | R1–R9 | Confirmación con fecha, cantidad y modal de correo simulado; sin envío real | `test_compra_en_efectivo_muestra_confirmacion_de_mail_simulado` |
| W4 | Comprar pases común y VIP | R4–R5 | Total calculado con precios y descuentos por edad | `test_compra_calcula_total_segun_pase_de_cada_visitante`, `test_compra_aplica_descuentos_por_edad` |
| W5 | Comprar con tarjeta | R6–R7 | Pantalla local de Mercado Pago simulado | `test_compra_con_tarjeta_muestra_checkout_simulado` |
| W6 | Omitir el medio de pago | R6 | Error visible y compra no registrada | `test_compra_sin_medio_de_pago_muestra_error_y_no_crea_compra` |
| W7 | Seleccionar una fecha pasada | R2 | Error visible y compra no confirmada | `test_compra_rechaza_fecha_anterior_a_hoy` |
| W8 | Solicitar más de 10 entradas para una fecha | R3 | Rechazo del máximo por transacción y del acumulado por usuario/fecha | `test_compra_rechaza_mas_de_diez_entradas`, `test_compra_rechaza_mas_de_diez_entradas_acumuladas_por_fecha` |
| W9 | Omitir edad o tipo de pase | R4 | Errores de validación visibles | `test_compra_rechaza_edad_o_tipo_de_pase_faltante` |
| W10 | Ver el formulario de compra | — | Forma de pago en sección aparte de los visitantes | `test_formulario_separa_forma_de_pago_de_datos_de_visitantes` |
| W11 | Elegir lunes | R2 | Rechazo porque el parque está cerrado | `test_compra_rechaza_los_lunes` |
| W12 | Crear y usar la cuenta compartida | R1 | Permite iniciar sesión, comprar y cerrar sesión | `test_cuenta_compartida_permite_iniciar_sesion_y_cerrar_sesion` |
| W13 | Ingresar letras en campos numéricos | R3–R4 | Se quitan en el navegador y el servidor rechaza datos inválidos | `test_compra_rechaza_letras_en_campos_numericos` |
| W14 | Ver el formato de fecha y campos numéricos | — | Calendario nativo en región argentina, fecha día/mes/año y teclado numérico | `test_formulario_muestra_fecha_dia_mes_anio_y_campos_solo_numericos` |
| W15 | Comprar para el mismo día alrededor de las 17:30 | R9 | Se acepta hasta las 17:30 inclusive y se rechaza después | `test_compra_mismo_dia_se_permite_hasta_las_1730`, `test_compra_mismo_dia_se_rechaza_despues_de_las_1730` |
| W16 | Seleccionar una fecha festiva o a más de un mes | R2 | Rechazo autoritativo y límite `max` en el calendario | `test_compra_rechaza_fechas_festivas`, `test_compra_rechaza_fecha_con_mas_de_un_mes_de_anticipacion`, `test_calendario_limita_fecha_maxima_y_muestra_reglas` |
| W17 | Aplicar descuentos en las edades límite | R4–R5 | Sin cargo hasta 3, mitad entre 4–15 y desde 60, tarifa completa entre 16–59 | `test_compra_aplica_descuentos_por_edad`, `test_compra_aplica_limites_de_descuento` |

## Datos de prueba

- Cada escenario crea su propio cliente y usa SQLite en memoria.
- Los precios predeterminados son $10.000 para común y $20.000 para VIP; se
  aplican los descuentos según edad.
- La compra no envía correo; la pantalla muestra un modal «Mail enviado
  (simulado)».
- La tarjeta se resuelve en una página local de compra de prueba y no realiza
  cargos reales.
- Las fechas válidas excluyen lunes, 25/12 y 1/1 y no superan un mes de
  anticipación.
- El calendario usa `type="date"` con idioma regional `es-AR`, para presentar
  la fecha como `dd/mm/aaaa`; el navegador envía el valor interno ISO
  `aaaa-mm-dd` al servidor.

## Resultado de los ciclos

El historial de las primeras iteraciones se conserva en la bitácora. La suite
actual cubre autenticación, fechas de apertura y anticipación, horario de corte,
precios, descuentos, límite acumulado, simulación de pago y confirmación visual
del correo. No se consideran válidas como RED fallas de importación,
configuración o dependencias.
