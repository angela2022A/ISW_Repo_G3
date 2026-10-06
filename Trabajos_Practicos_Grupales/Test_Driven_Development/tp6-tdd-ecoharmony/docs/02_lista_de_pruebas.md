# 02 — Lista de pruebas (Test List)

Escrita **antes** de implementar, siguiendo el patrón *Test List* ("primero escribe la lista de tests que vas a realizar").
Los casos derivados se obtuvieron con **partición de equivalencias** y **análisis de valores límite**.

## Pruebas de usuario de la US (obligatorias)

| ID | Prueba de usuario | Regla | Resultado esperado | Test |
|---|---|---|---|---|
| U1 | Inscribirse a una actividad con cupo, horario válido, datos completos, T&C aceptados y recepción del email | R1–R8 | pasa | `test_inscripcion_valida_devuelve_los_datos_de_la_inscripcion` + `test_inscripcion_exitosa_envia_email_con_qr` |
| U2 | Inscribirse a una actividad sin cupo en el horario | R3 | falla — `SinCupoError` | `test_inscripcion_a_horario_sin_cupo_falla` |
| U3 | Inscribirse sin talla en una actividad que no la requiere | R6 | pasa | `test_inscripcion_sin_talla_en_actividad_que_no_la_requiere_pasa` |
| U4 | Inscribirse en un horario con el parque cerrado o la actividad no disponible | R2 | falla — `HorarioNoDisponibleError` | `test_inscripcion_en_horario_no_disponible_falla` |
| U5 | Inscribirse sin aceptar T&C | R7 | falla — `TerminosNoAceptadosError` | `test_inscripcion_sin_aceptar_terminos_falla` |
| U6 | Inscribirse sin talla en una actividad que la requiere | R6 | falla — `TallaRequeridaError` | `test_inscripcion_sin_talla_requerida_por_la_actividad_falla` |

## Casos derivados de los criterios de aceptación

| ID | Caso | Regla | Técnica | Resultado esperado | Test |
|---|---|---|---|---|---|
| D1 | Actividad fuera del listado (`'Buceo'`, vacía, `None`) | R1 | Partición — clase inválida | falla | `test_inscripcion_a_actividad_fuera_del_listado_falla` |
| D2 | Cupo restante = 3, se inscriben 3 | R3 | Valor límite (borde válido) | pasa | `test_inscripcion_que_ocupa_exactamente_el_cupo_restante_pasa` |
| D3 | Cupo restante = 3, se inscriben 4 | R3 | Valor límite (borde inválido) | falla | `test_inscripcion_que_supera_en_uno_el_cupo_restante_falla` |
| D4 | Cantidad de personas = 0 | S4 | Valor límite | falla | `test_inscripcion_con_cero_personas_falla` |
| D5 | Cantidad declarada ≠ visitantes cargados | S4 | Partición | falla | `test_inscripcion_con_cantidad_distinta_a_visitantes_falla` |
| D6 | Visitante sin nombre, DNI o edad | R5 | Partición — una clase inválida por dato | falla | `test_inscripcion_con_visitante_incompleto_falla` |
| D7 | Tras una inscripción exitosa el cupo baja | S3 | Comportamiento | cupo 10 → 8 | `test_inscripcion_exitosa_descuenta_los_cupos` |
| D8 | Si la inscripción se rechaza, no se envía email | S6 | Comportamiento (mock) | email no enviado | `test_inscripcion_rechazada_no_envia_email` |

## Clases de equivalencia

| Entrada | Válidas | Inválidas |
|---|---|---|
| Actividad | {Tirolesa, Safari, Palestra, Jardinería} | fuera del listado, vacía, nula |
| Horario | horarios de la actividad | parque cerrado, actividad no opera |
| Cantidad de personas | 1 ≤ n ≤ cupo restante y n = visitantes cargados | 0, n > cupo restante, n ≠ visitantes |
| Datos del visitante | nombre, DNI y edad presentes | falta alguno |
| Talla | presente; ausente si la actividad no la requiere | ausente si la actividad la requiere |
| T&C | aceptados | no aceptados |
