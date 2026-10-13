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

## Decisiones que emerjan del ciclo

| Etapa | Decisión / refactor | Motivo |
|---|---|---|
| RED | Pendiente de ejecución | — |
| GREEN | Pendiente | — |
| REFACTOR | Pendiente | — |
