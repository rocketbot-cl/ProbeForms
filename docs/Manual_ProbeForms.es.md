# ProbeForms
  
Módulo para generar formularios offline y enviar la información a Rocketbot  

*Read this in other languages: [English](Manual_ProbeForms.md), [Português](Manual_ProbeForms.pr.md), [Español](Manual_ProbeForms.es.md)*
  
![banner](imgs/Banner_ProbeForms.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

ProbeForms es una herramienta que permite crear formularios para recolectar información de los usuarios.

### Cómo funciona

Al descargar el módulo de ProbeForms, este incluye un ejecutable que inicia un servidor local para servir el formulario. El ejecutable se encuentra en la carpeta `Rocketbot/modules/ProbeForms/libs/bin`.

Existen dos métodos para editar los campos del formulario.

#### Método 1 (Recomendado)

Dentro de la carpeta del módulo, en `libs/bin/_internal/static/` encontrarás el archivo index.html, que presenta el formulario de forma visual. Este archivo te permite editar directamente el contenido dentro de la etiqueta `<form action="/submit" method="post" id="probeForm">`, donde podrás personalizar los campos según tus necesidades. La información es enviada al endpoint correspondiente a través de la etiqueta `<script>`. Se recomienda no modificar este script para asegurar que los datos sean enviados correctamente.
Dentro de la etiqueta 
`<script>` también se encuentran las funciones que se ejecutan en el servicio de ProbeForms para obtener la ruta de archivos y carpetas. Se recomienda no modificarlas para asegurar el correcto funcionamiento del módulo.

#### Método 2

Alternativamente, puedes crear un archivo forms.json en la misma carpeta `libs/bin/_internal/static/`. Este archivo te permite definir los campos del formulario siguiendo una estructura predefinida.

##### Estructura de form.json

Para generar un formulario correctamente a partir de un archivo form.json, es necesario respetar la siguiente estructura:

```json
{
    "title": "Formulario de ejemplo",
    "inputs": [
        {
            "type": "input",
            "title": "Ingresa tu nombre",
            "id": "name",
            "format": "text",
            "column-class": "col-md-12",
            "css": "text-alert",
            "required": true
        }
    ],
    "submit": {
        "title": "Enviar",
        "css": "btn btn-primary"
    }
}
```


El archivo form.json es procesado por ProbeForms para generar un formulario HTML en el archivo index.html. Los campos del formulario se definen en el array `inputs`, donde cada objeto representa un campo. El objeto `submit` define el botón de envío.

##### Detalles de los campos del formulario

- **title**: Título del formulario

- **inputs**: Los diferentes campos de información que el usuario podrá completar. Las opciones disponibles y sus diferentes campos son los siguientes:
    - **type**: Indica el tipo de input a utilizar en el formulario. Opciones disponibles: label, input, select, select, checkbox, textarea, radio
    - **title**: Título del input.
    - **id**: Identificador único del input. No debe ser duplicado ya que corresponde a la clave del json en el resultado retornado.
    - **format**: Solo disponible en entradas de tipo input. Sus opciones son text, password, email.
    - **column-class**: Clase css de Bootstrap que tendrá el contenedor del input. Por defecto col-md-12
    - **css**: Clases css de Bootstrap que tendrá el input.
    - **required**: Indica si el input es requerido. Por defecto false

- **submit**: Esta sección permite modificar el texto y estilo del botón que envía el formulario. Las opciones disponibles son las siguientes:
    - **title**: Texto que tendrá el botón.
    - **css**: Clases css de Bootstrap que darán el estilo deseado al botón.

> 💡 **Nota**: Si se utiliza un archivo `form.json` para generar el formulario, el contenido del archivo `index.html` será reemplazado en cada ejecución del módulo. Se recomienda guardar una copia de `index.html` si se está en proceso de pruebas.

### Generación y Uso del Formulario

Una vez definido el archivo form.json, el formulario puede ser generado y mostrado ejecutando el módulo de ProbeForms. Esto iniciará el servicio local y abrirá el formulario en el navegador predeterminado.

#### Recepción de datos

Cuando el formulario es enviado, los datos serán almacenados en memoria mientras ProbeForms se encuentra en ejecución. Estos datos pueden ser recuperados utilizando el comando Esperar por Mensaje en un modelo FIFO (First In First Out). Si no hay datos disponibles en una petición GET, la petición permanecerá pendiente hasta que los datos estén completos o se alcance el timeout definido.


## Descripción de los comandos

### Ejecutar ProbeForms
  
Este comando permite ejecutar el servicio de ProbeForms.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Puerto|Puerto en el que se ejecutará el servicio de ProbeForms|4321|

### Esperar submit
  
Este comando permite esperar a que se envíe un formulario de ProbeForms.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tiempo de espera máximo (segundos)|Tiempo máximo que esperará el robot por un mensaje|3600|
|Puerto|Puerto en el que se ejecutará el servicio de ProbeForms|4321|
|Asignar resultado a variable|Nombre de la variable de tu robot que guardará el resultado del formulario|variable|

### Cerrar ProbeForms
  
Este comando permite cerrar el servicio de ProbeForms.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
