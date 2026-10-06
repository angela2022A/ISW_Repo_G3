# 01 — Concepto de la US

## User Story

> **Inscribirme a actividad** (5 SP)
> COMO visitante QUIERO inscribirme a una actividad PARA reservar mi lugar en la misma.

## Reglas de negocio (derivadas de los criterios de aceptación)

| # | Regla | Criterio de aceptación de origen |
|---|---|---|
| R1 | La actividad debe pertenecer al listado: Tirolesa, Safari, Palestra, Jardinería | "Debe requerir seleccionar una actividad del conjunto…" |
| R2 | El horario debe estar dentro de los disponibles de la actividad | "Debe requerir seleccionar el horario dentro de los disponibles" |
| R3 | Debe haber cupo suficiente en ese horario para todas las personas | "…siempre y cuando tengan cupos disponibles para el horario seleccionado" |
| R4 | Se indica la cantidad de personas que participan | "Debe indicar la cantidad de personas…" |
| R5 | Por cada persona: nombre, DNI y edad obligatorios | "Para cada persona… nombre, DNI, edad…" |
| R6 | Talla de vestimenta obligatoria solo si la actividad la exige | "…y talla de vestimenta si la actividad lo demanda" |
| R7 | Deben aceptarse los términos y condiciones de la actividad | "Debe requerir aceptar los términos y condiciones…" |
| R8 | Al finalizar, se envía un email con la información de la inscripción y un código QR | "Al finalizar la inscripción, se debe enviar un correo…" |

## Supuestos del grupo

La US no define estos puntos. Los fijamos para poder escribir pruebas con datos concretos:

| # | Supuesto | Motivo |
|---|---|---|
| S1 | Tirolesa y Palestra requieren talla (arnés / equipo); Safari y Jardinería no | La US no indica cuáles la requieren |
| S2 | El parque abre de 09:00 a 18:00 y cada actividad tiene horarios fijos dentro de esa franja (ver `tests/conftest.py`) | Necesario para probar U4 |
| S3 | Los cupos son por actividad y por horario, y se descuentan al inscribirse | Sin descuento la regla R3 no tendría efecto |
| S4 | La cantidad de personas debe ser ≥ 1 y coincidir con la cantidad de visitantes cargados | Coherencia entre R4 y R5 |
| S5 | El email se envía al visitante que realiza la inscripción (usuario ya identificado); la dirección la resuelve el notificador | La US no pide ingresar un email |
| S6 | Si la inscripción se rechaza, no se descuentan cupos ni se envía email | Consecuencia lógica de R3 y R8 |

## Fuera de alcance

- Edad mínima por actividad: no figura en los criterios de aceptación.
- Validación de formato de DNI: solo se exige que esté presente.
- Envío real de emails y generación real del QR: se reemplazan por dobles de prueba (ver `04_decisiones_de_diseno.md`).
- Interfaz de usuario: la US se ejercita llamando directamente a `inscribir_actividad(...)`.
