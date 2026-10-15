# 04 — Decisiones de diseño

## Decisiones iniciales

### D-01. Python + Django

Django brinda formularios HTTP, sesiones y autenticación para la aplicación web
server-rendered. Las pruebas usan su cliente HTTP y una base SQLite en memoria.

### D-02. Acceso autenticado

La compra requiere que el visitante cree una cuenta con email y contraseña e
inicie sesión antes de acceder al formulario de compra.

### D-03. Precios y descuentos configurables

Los precios común y VIP se leen de configuración, no de literales dispersos en
las vistas. Se aplican los descuentos por edad en el cálculo del servidor y en
el total estimado del formulario.

### D-04. Integraciones simuladas

La compra muestra un modal de correo simulado y una pantalla local de Mercado
Pago de prueba. El flujo de compra no envía mensajes ni realiza transacciones
reales.

### D-05. Validación antes de confirmar

Fecha, cantidad, edad, pase y medio de pago se validan antes de registrar la
compra simulada.

### D-06. Días y horizonte de compra

El parque cierra los lunes, el 25 de diciembre y el 1 de enero; admite fechas
hasta un mes adelante. Para el mismo día, la compra cierra a las 17:30. El
navegador da feedback inmediato y el servidor vuelve a validar las reglas.

### D-07. SMTP configurable para reenvío manual

La configuración SMTP se conserva para el comando manual de reenvío, pero el
recorrido de compra no envía correo. Las credenciales se leen del entorno y no
se incluyen en el repositorio.

### D-08. Guía de estilo de código
El código sigue la guía seleccionada por el grupo en el TP2: PEP 8. Se
respetan líneas de hasta 79 caracteres, imports al inicio del archivo y
nombres en snake_case.


## Decisiones que emerjan del ciclo

| Etapa | Decisión / refactor | Motivo |
|---|---|---|
| RED | Se escribieron nueve pruebas HTTP contra la aplicación Django | Verificar los criterios desde las rutas que usa un visitante |
| GREEN | Se agregó una aplicación server-rendered con vistas, plantillas, autenticación y una tabla persistente de compras | Hacer pasar las pruebas web y permitir ejecutar la aplicación en local |
| GREEN (histórico) | En una iteración anterior, el efectivo enviaba correo y la tarjeta quedaba pendiente en una URL de checkout | Esta implementación se reemplazó por las simulaciones locales documentadas abajo |
| GREEN | El formulario calcula un total estimado en el navegador y vuelve a calcular el total en el servidor | Mostrar el importe al visitante y conservar el cálculo autoritativo al recibir la compra |
| REFACTOR | La validación de fecha, cantidad y cada visitante se separó en funciones privadas específicas | Facilitar lectura y mantenimiento de `validar_compra` sin alterar reglas ni respuestas |
| Compatibilidad | Se bajó el mínimo a Python 3.9 y Django 4.2 (`from __future__ import annotations` y `USE_TZ = True` explícito en la configuración de pruebas) | Permitir que todos los integrantes ejecuten el proyecto con su versión de Python, sin cambiar el comportamiento en Django 5 |
| RED (ciclo 2, histórico) | Se probó el envío de correo en la compra | La implementación actual muestra confirmación simulada; no hace envío |
| REFACTOR (ciclo 2) | Se elimina el destinatario fijo `EMAIL_CONFIRMATION_RECIPIENT` y los textos de mail simulado | Evitar configuración sin uso y documentación desactualizada |
| RED/GREEN (ciclo 3, histórico) | Se probó una redirección externa de pago con un mail previo | Reemplazado por la página local de checkout simulado; no hay cargo ni mail |
| Actualización de dominio | Se reemplazan los días hábiles por cierre los lunes/25-12/1-1; se agrega horizonte de un mes, corte 17:30, precios y descuentos confirmados, y tope acumulado por fecha | Alinear la implementación con las respuestas de PO |
| Simulación de desarrollo | El checkout de tarjeta es una pantalla local y el mail se confirma con un modal; no se hacen cobros ni envíos reales desde la compra | Evitar integraciones externas en el recorrido de prueba |
