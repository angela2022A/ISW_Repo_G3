# 04 — Decisiones de diseño

## Decisiones iniciales

### D-01. Python + Django

Django brinda formularios HTTP, sesiones y autenticación para la aplicación web
server-rendered. Las pruebas usan su cliente HTTP y una base SQLite en memoria.

### D-02. Acceso autenticado

La compra requiere que el visitante cree una cuenta con email y contraseña e
inicie sesión antes de acceder al formulario de compra.

### D-03. Precios configurables

Los precios regular y VIP son valores provisorios que se leen de configuración,
no literales dispersos en las vistas. Los valores de pruebas se fijan mediante
configuración específica de test.

### D-04. Integraciones externas aisladas

El correo se verifica con el backend local de pruebas. El flujo de pago con
tarjeta verifica la redirección a una URL de Mercado Pago configurable y no
realiza transacciones reales durante las pruebas.

### D-05. Validación antes de confirmar

Fecha, cantidad, edad, pase y medio de pago se validan antes de confirmar compra,
enviar email o redirigir a la pasarela.

### D-06. Días de apertura

El parque admite compras para fechas hábiles de lunes a viernes. La regla se
valida tanto en el navegador como en el servidor, que es la validación
autoritaria.

### D-07. Envío de correo configurable

En desarrollo se conserva el backend de consola. Al configurar `EMAIL_HOST` se
activa SMTP, con host, puerto, TLS, usuario y contraseña leídos del entorno. Las
credenciales no se incluyen en el repositorio; las pruebas continúan usando el
backend local de Django.

### D-08. Guía de estilo de código
El código sigue la guía seleccionada por el grupo en el TP2: PEP 8. Se
respetan líneas de hasta 79 caracteres, imports al inicio del archivo y
nombres en snake_case.


## Decisiones que emerjan del ciclo

| Etapa | Decisión / refactor | Motivo |
|---|---|---|
| RED | Se escribieron nueve pruebas HTTP contra la aplicación Django | Verificar los criterios desde las rutas que usa un visitante |
| GREEN | Se agregó una aplicación server-rendered con vistas, plantillas, autenticación y una tabla persistente de compras | Hacer pasar las pruebas web y permitir ejecutar la aplicación en local |
| GREEN | Una compra en efectivo queda confirmada y envía correo; una compra con tarjeta queda pendiente y deriva a la URL de checkout configurada | No considerar pagado un pedido antes de que lo confirme la pasarela externa |
| GREEN | El formulario calcula un total estimado en el navegador y vuelve a calcular el total en el servidor | Mostrar el importe al visitante y conservar el cálculo autoritativo al recibir la compra |
| REFACTOR | La validación de fecha, cantidad y cada visitante se separó en funciones privadas específicas | Facilitar lectura y mantenimiento de `validar_compra` sin alterar reglas ni respuestas |
| Compatibilidad | Se bajó el mínimo a Python 3.9 y Django 4.2 (`from __future__ import annotations` y `USE_TZ = True` explícito en la configuración de pruebas) | Permitir que todos los integrantes ejecuten el proyecto con su versión de Python, sin cambiar el comportamiento en Django 5 |
| RED (ciclo 2) | La prueba de compra en efectivo pasa a exigir un mail al usuario y se elimina la prueba que exigía no enviar correo | El criterio de aceptación pide enviar un mensaje de confirmación vía mail |
| GREEN (ciclo 2) | La compra en efectivo envía el mail al email del usuario autenticado, con cantidad, fecha (dd/mm/aaaa) y total, reutilizando `enviar_confirmacion_compra` | Cumplir el criterio con el código mínimo; en las pruebas el mail se captura en memoria y no se envía nada real |
| REFACTOR (ciclo 2) | Se elimina el destinatario fijo `EMAIL_CONFIRMATION_RECIPIENT` y los textos de mail simulado | Evitar configuración sin uso y documentación desactualizada |
| RED (ciclo 3) | Una compra con tarjeta redirige a Mercado Pago y envía el mail de confirmación | La prueba de usuario exige recibir el mail también al pagar con tarjeta |
| GREEN (ciclo 3) | Con tarjeta, el mail se envía justo después de registrar la compra y antes de redirigir a Mercado Pago | Al redirigir, el usuario sale de la aplicación y no está implementado el aviso de vuelta de Mercado Pago (webhook); si el mail se enviara después del pago, nunca saldría. Limitaciones: el mail confirma la solicitud de compra, no el pago aprobado (la compra queda «pendiente de pago»), y si falla el envío la compra queda registrada igual y el usuario ve un error |
| REFACTOR (ciclo 3) | El envío de efectivo y tarjeta se unificó en una sola llamada a `enviar_confirmacion_compra`, justo después de crear la compra (`views.py`) | Evitar código repetido entre los dos medios de pago |
