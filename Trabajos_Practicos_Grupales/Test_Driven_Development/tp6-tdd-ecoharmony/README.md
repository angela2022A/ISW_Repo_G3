# EcoHarmony Park — guía para probar el proyecto

Aplicación web en Python y Django para registrar usuarios y comprar entradas
para EcoHarmony Park. Esta guía explica cómo abrir, ejecutar y probar el
proyecto desde Visual Studio Code en Windows.

## Requisitos

- Visual Studio Code.
- Python 3.10 o superior.
- La extensión **Python** de Microsoft para VS Code.
- Git, para clonar el repositorio.

## Abrir el proyecto en Visual Studio Code

1. Cloná el repositorio si todavía no lo tenés:

   ```powershell
   git clone <URL-del-repositorio>
   ```

2. En VS Code, elegí **Archivo → Abrir carpeta...** y seleccioná
   `tp6-tdd-ecoharmony` (la carpeta que contiene `manage.py`).
3. Abrí la terminal integrada desde **Terminal → Nuevo terminal**. Los comandos
   de esta guía se ejecutan desde esa carpeta.

## Preparar el entorno

En la terminal integrada de VS Code, seleccioná PowerShell y ejecutá:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

Si PowerShell no reconoce `py`, probá `python -m venv .venv`. Si bloquea la
activación del entorno virtual, ejecutá este comando en esa terminal y volvé a
activar `.venv`:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

En VS Code, elegí el intérprete del proyecto:

1. Presioná `Ctrl+Shift+P`.
2. Ejecutá **Python: Select Interpreter**.
3. Seleccioná el Python que se encuentra en
   `.venv\Scripts\python.exe`.

Si esa opción no aparece, verificá que la extensión Python de Microsoft esté
instalada y recargá la ventana de VS Code.

## Iniciar la aplicación

En la terminal integrada, con `.venv` activado:

```powershell
python manage.py runserver
```

Abrí <http://127.0.0.1:8000/> en el navegador. Para apagar el servidor, volvé a
la terminal y presioná `Ctrl+C`.

## Iniciar sesión

Podés crear una cuenta desde **Registrarse** en la aplicación. También existe
un usuario genérico para pruebas:

- **Email/usuario:** `ecoharmony.g3.pruebas@yopmail.com`
- **Contraseña en la base local ya configurada:** `test123`

`test123` es una contraseña débil para demostración local; no la uses en otros
sistemas ni para información real. Las credenciales y la base de datos no se
comparten al clonar o actualizar el repositorio: `db.sqlite3` es local y está
excluida de Git. Por eso, en una computadora nueva esa misma contraseña puede
no funcionar.

Para crear el usuario genérico en una base local nueva, primero ejecutá
`python manage.py migrate` y luego:

```powershell
python manage.py crear_usuario_compartido
```

El comando genera una contraseña aleatoria si la cuenta no existe. La muestra
una sola vez en la terminal; guardala localmente y compartila con el grupo por
un medio privado. Si el usuario ya existe, el comando no cambia su contraseña.
También podés registrarte con una cuenta propia desde la web.

## Recorrido de prueba de compra

1. Registrate en `/registro/` o iniciá sesión en `/iniciar-sesion/`.
2. Abrí **Comprar entradas**.
3. Seleccioná una fecha desde hoy hasta un mes de anticipación. El parque cierra
   los lunes, el 25 de diciembre y el 1 de enero; la compra para el mismo día
   está disponible hasta las 17:30. El navegador configurado en español de
   Argentina muestra la fecha como día/mes/año.
4. Indicá entre 1 y 10 entradas por transacción. Para cada visitante visible,
   ingresá la edad y elegí el pase Común o VIP. El límite total por usuario y
   fecha es de 10 entradas, incluso si se hacen varias compras.
5. Seleccioná la forma de pago y verificá el total estimado.
6. Enviá la compra. Para efectivo se muestra la confirmación con la cantidad,
   la fecha y el total. Para tarjeta se muestra el checkout simulado de Mercado
   Pago. Ambos recorridos muestran la confirmación de correo simulada.

### Comportamientos a comprobar

- Las fechas pasadas, los lunes, el 25 de diciembre y el 1 de enero se rechazan
  también en el servidor.
- Cantidad y edades son campos numéricos: se eliminan letras al escribir y el
  servidor vuelve a validar lo recibido.
- La forma de pago aparece en una sección separada de los visitantes.
- Los precios predeterminados son `$10.000` para Común y `$20.000` para VIP.
- Hasta 3 años no pagan; de 4 a 15 años y desde los 60 años tienen 50% de
  descuento.
- Cada usuario puede comprar como máximo 10 entradas para una fecha, sumando
  todas sus transacciones.
- La tarjeta muestra una pantalla local de Mercado Pago simulado. **No procesa
  pagos reales.**
- La confirmación muestra el modal **“Mail enviado (simulado)”**. La compra no
  envía correos reales.

## Ejecutar las pruebas desde VS Code

Con `.venv` seleccionado y activado, ejecutá en la terminal integrada:

```powershell
python -m pytest
```

Las pruebas usan una base temporal y no envían correos ni realizan pagos
reales. También podés correrlas desde el panel **Testing/Pruebas** de VS Code,
si la extensión Python ya detectó pytest. Para verificar la configuración de
Django:

```powershell
python manage.py check
```

## Datos locales y documentación

- `db.sqlite3`, usuarios y compras pertenecen a cada computadora; no se
  sincronizan entre compañeros.
- La lista de escenarios de prueba está en
  [`docs/02_lista_de_pruebas.md`](docs/02_lista_de_pruebas.md).
- La nota sobre correo simulado y SMTP está en
  [`docs/05_configuracion_correo.md`](docs/05_configuracion_correo.md).
