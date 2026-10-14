# Crear el usuario genérico compartido

Cada integrante debe crear el usuario en su propia base de datos local. Desde
PowerShell, en la carpeta del proyecto, ejecutá:

```powershell
python manage.py crear_usuario_compartido
```

Si todavía no existe, el comando la crea y genera una contraseña aleatoria que
se muestra una sola vez. Guardala y compartila con el grupo por un medio privado,
no en el repositorio. Para crear la misma cuenta en la base de otro integrante,
esa persona debe proporcionar la contraseña acordada en su PowerShell y correr
el comando:

```powershell
$claveCompartida = Read-Host "Contraseña compartida" -AsSecureString
$env:ECOHARMONY_SHARED_USER_PASSWORD = [System.Net.NetworkCredential]::new("", $claveCompartida).Password
python manage.py crear_usuario_compartido
```

El comando no cambia la contraseña ni revela credenciales si la cuenta ya
existe. Luego, cerrá la sesión personal en EcoHarmony y entrá con el correo
`ecoharmony.g3.pruebas@yopmail.com` y la contraseña compartida. El encabezado
mostrará ese correo. La cuenta y su contraseña son solo para pruebas locales;
la bandeja YOPmail es pública y no debe usarse con información sensible.

## Mailtrap Email Sandbox (solo pruebas)

Mailtrap Sandbox captura los mensajes en su inbox de pruebas; no los entrega a
YOPmail ni a la dirección destinataria. La dirección YOPmail queda visible como
destinatario del mensaje dentro del sandbox. Las bandejas YOPmail son públicas,
por lo que este destino debe usarse solo con información ficticia.

En Windows, desde PowerShell y la carpeta del proyecto, copiá las credenciales
SMTP mostradas en **My Sandbox → SMTP**. No guardes la contraseña SMTP en el
repositorio ni la compartas:

```powershell
$env:EMAIL_HOST = "sandbox.smtp.mailtrap.io"
$env:EMAIL_PORT = "587"
$env:EMAIL_USE_TLS = "true"
$env:EMAIL_USE_SSL = "false"
$env:EMAIL_HOST_USER = Read-Host "Usuario SMTP de Mailtrap"
$claveSmtp = Read-Host "Contraseña SMTP de Mailtrap" -AsSecureString
$env:EMAIL_HOST_PASSWORD = [System.Net.NetworkCredential]::new("", $claveSmtp).Password
$env:DEFAULT_FROM_EMAIL = "ecoharmony@example.test"
python manage.py runserver
```

Estas variables solo se aplican en esa ventana de PowerShell. Cada integrante
del grupo debe configurar sus propias credenciales de Mailtrap antes de iniciar
el servidor. Si Django ya estaba corriendo, detenelo con `Ctrl+C` y reinicialo
después de definirlas.

La pantalla de compra no envía automáticamente mensajes. Para probar
Sandbox, ejecutá el comando manual de reenvío indicado en la sección de Gmail,
con las variables de SMTP de Sandbox y un ID de compra confirmado en efectivo.
El mensaje aparecerá en el inbox de Mailtrap, pero no llegará a YOPmail.

Las credenciales de **My Sandbox** nunca entregan a YOPmail: solo capturan el
mensaje dentro del inbox del sandbox.

## Envío real usando Gmail como remitente

Si no tenés un dominio propio, podés probar con una cuenta Gmail como
remitente. Google exige tener activada la verificación en dos pasos y crear una
contraseña de aplicación de 16 caracteres; no uses la contraseña normal de
Google. La opción puede no estar disponible para algunas cuentas. Consultá
[Crear y usar contraseñas de aplicación](https://support.google.com/accounts/answer/185833?hl=es).

La contraseña de aplicación es un secreto: ingresala directamente en tu
PowerShell, no la pegues en el chat ni la guardes en el repositorio. Detené
primero el servidor Django existente con `Ctrl+C`. Luego, en PowerShell y desde
la carpeta del proyecto, configurá el envío y reenviá la compra más reciente de
la captura (ID `8`):

```powershell
$env:EMAIL_HOST = "smtp.gmail.com"
$env:EMAIL_PORT = "587"
$env:EMAIL_USE_TLS = "true"
$env:EMAIL_USE_SSL = "false"
$env:EMAIL_HOST_USER = Read-Host "Tu dirección Gmail"
$claveAplicacion = Read-Host "Contraseña de aplicación de Google" -AsSecureString
$env:EMAIL_HOST_PASSWORD = [System.Net.NetworkCredential]::new("", $claveAplicacion).Password
Remove-Variable claveAplicacion
$env:DEFAULT_FROM_EMAIL = $env:EMAIL_HOST_USER
python manage.py reenviar_confirmacion 8
```

Si el comando indica que el servidor SMTP aceptó el mensaje, actualizá la
bandeja YOPmail y revisá también spam. La aceptación SMTP no garantiza que
YOPmail muestre el mensaje; los buzones descartables pueden filtrarlo. Ejecutá
el comando una sola vez para no duplicar la confirmación. Para probar compras
nuevas con envío automático, el código debe volver a habilitarse explícitamente;
actualmente está desactivado.

```powershell
python manage.py runserver
```

Estas variables solo existen en esa ventana de PowerShell. Cada integrante
debe configurar su propio remitente y contraseña de aplicación. El remitente
será tu dirección Gmail personal, aunque la sesión de EcoHarmony siga usando
el usuario genérico. No uses la contraseña normal de Google.

## Envío real con Mailtrap Email Sending

Para entregar a YOPmail, hace falta **API/SMTP → Sending Setup → Transactional
Stream**, no las credenciales de **Sandboxes**. Mailtrap requiere agregar y
verificar un dominio de envío que el grupo controle y usar un remitente de ese
dominio. No se puede verificar `yopmail.com` porque el grupo no controla ese
dominio. Mailtrap publica los registros DNS necesarios para verificar el
dominio; deben agregarse en su proveedor de DNS antes de usar las credenciales
de envío.

En la página de Sending Setup, seleccioná el dominio verificado, Transactional
Stream y SMTP. Para Mailtrap Email Sending, la configuración documentada usa
`live.smtp.mailtrap.io`, puerto `587`, usuario `api` y el token SMTP/API como
contraseña. Usá el remitente que Mailtrap autorizó para el dominio verificado.
En PowerShell, ejecutá esto desde la carpeta del proyecto; el token se solicita
sin mostrarlo y las variables solo permanecen en esa ventana:

```powershell
$env:EMAIL_HOST = "live.smtp.mailtrap.io"
$env:EMAIL_PORT = "587"
$env:EMAIL_USE_TLS = "true"
$env:EMAIL_USE_SSL = "false"
$env:EMAIL_HOST_USER = "api"
$tokenSmtp = Read-Host "Token SMTP de Mailtrap Email Sending" -AsSecureString
$env:EMAIL_HOST_PASSWORD = [System.Net.NetworkCredential]::new("", $tokenSmtp).Password
Remove-Variable tokenSmtp
$env:DEFAULT_FROM_EMAIL = Read-Host "Remitente verificado (por ejemplo, entradas@tu-dominio.com)"
python manage.py runserver
```

Detené primero cualquier servidor Django que ya esté corriendo con `Ctrl+C`.
Luego hacé una compra nueva en efectivo. Para volver a enviar la última compra
confirmada en efectivo guardada en esa base local, ejecutá en otra ventana de
PowerShell con las mismas variables configuradas:

```powershell
python manage.py reenviar_confirmacion
```

También podés pasar el ID de compra explícitamente:

```powershell
python manage.py reenviar_confirmacion 1
```

El comando se niega a enviar si el backend no es SMTP o si no encuentra una
compra en efectivo confirmada. Que el proveedor acepte el mensaje no garantiza
que YOPmail lo muestre; revisá los registros de Email Sending y la carpeta de
spam. La bandeja de YOPmail es pública: no envíes información personal o de
pago.

Las pruebas automatizadas usan el backend local de Django y verifican que el
destinatario sea el configurado; no envían correo real. Las compras con tarjeta
siguen pendientes de la integración real con Mercado Pago, por lo que no
generan email de pago confirmado.
