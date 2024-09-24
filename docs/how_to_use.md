
## How to use this module

ProbeForms is a tool that allows you to create forms to collect information from users.

### How it works

When you download the ProbeForms module, it includes an executable that starts a local server to serve the form. The executable is located in the `Rocketbot/modules/ProbeForms/libs/bin` folder.

There are two methods for editing the form fields.

#### Method 1 (Recommended)

Inside the module folder, in `libs/bin/_internal/static/` you will find the index.html file, which presents the form visually. This file allows you to directly edit the content inside the `<form action="/submit" method="post" id="probeForm">` tag, where you can customize the fields according to your needs. The information is sent to the corresponding endpoint through the `<script>` tag. It is recommended that you do not modify this script to ensure that the data is sent correctly.

#### Method 2

Alternatively, you can create a forms.json file in the same `libs/bin/_internal/static/` folder. This file allows you to define the form fields following a predefined structure.

##### Structure of form.json

To generate a form correctly from a form.json file, it is necessary to respect the following structure:

```json
{
    "title": "Example form",
    "inputs": [
        {
            "type": "input",
            "title": "Enter your name",
            "id": "name",
            "format": "text",
            "column-class": "col-md-12",
            "css": "text-alert",
            "required": true
        }
    ],
    "submit": {
        "title": "Submit",
        "css": "btn btn-primary"
    }
}
```

The form.json file is processed by ProbeForms to generate an HTML form in the index.html file. The form fields are defined in the `inputs` array, where each object represents a field. The `submit` object defines the submit button.

##### Details of the form fields

- **title**: Title of the form

- **inputs**: The different information inputs that the user will be able to complete. The available options and their different fields are the following:
  - **type**: Indicates the type of input to be used in the form. Available options: label, input, select, select, checkbox, textarea, radio
  - **title**: Title of the input.
  - **id**: Unique identifier of the input. It must not be duplicated since it corresponds to the key of the json in the returned result.
  - **format**: Only available in input type entries. Its options are text, password, email.
  - **column-class**: Bootstrap css class that will have the input container. By default col-md-12
  - **css**: Bootstrap css classes that the input will have.
  - **required**: Indicates if the input is required. Default false

- **submit**: This section allows you to modify the text and style of the button that submits the form. The available options are the following:
  - **title**: Text that the button will have.
  - **css**: Bootstrap css classes that will give the desired style to the button.

> 💡 **Note**: If a `form.json` file is used to generate the form, the content of the `index.html` file will be replaced at each module execution. It is recommended to save a copy of `index.html` if testing is in progress.

### Form Generation and Use

Once the form.json file is defined, the form can be generated and displayed by running the ProbeForms module. This will start the local service and open the form in the default browser.

#### Receipt of data

When the form is submitted, the data will be stored in memory while ProbeForms is running. This data can be retrieved using the Wait for Message command in a FIFO (First In First Out) model. If no data is available in a GET request, the request will remain pending until the data is completed or the defined timeout is reached.

---

## Como usar este modulo

ProbeForms es una herramienta que permite crear formularios para recolectar información de los usuarios.

### Cómo funciona

Al descargar el módulo de ProbeForms, este incluye un ejecutable que inicia un servidor local para servir el formulario. El ejecutable se encuentra en la carpeta `Rocketbot/modules/ProbeForms/libs/bin`.

Existen dos métodos para editar los campos del formulario.

#### Método 1 (Recomendado)

Dentro de la carpeta del módulo, en `libs/bin/_internal/static/` encontrarás el archivo index.html, que presenta el formulario de forma visual. Este archivo te permite editar directamente el contenido dentro de la etiqueta `<form action="/submit" method="post" id="probeForm">`, donde podrás personalizar los campos según tus necesidades. La información es enviada al endpoint correspondiente a través de la etiqueta `<script>`. Se recomienda no modificar este script para asegurar que los datos sean enviados correctamente.

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

---

## Como usar este módulo

ProbeForms é uma ferramenta que permite criar formulários para coletar informações dos usuários.

### Como funciona

Ao baixar o módulo ProbeForms, ele inclui um executável que inicia um servidor local para servir o formulário. O executável está localizado na pasta `Rocketbot/modules/ProbeForms/libs/bin`.

Existem dois métodos para editar os campos do formulário.

#### Método 1 (Recomendado)

Dentro da pasta do módulo, em `libs/bin/_internal/static/`, você encontrará o arquivo index.html, que apresenta o formulário visualmente. Este arquivo permite que você edite diretamente o conteúdo dentro da tag `<form action="/submit" method="post" id="probeForm">`, onde você pode personalizar os campos de acordo com suas necessidades. As informações são enviadas para o endpoint correspondente através da tag `<script>`. Recomenda-se não modificar este script para garantir que os dados sejam enviados corretamente.

#### Método 2

Alternativamente, você pode criar um arquivo forms.json na mesma pasta `libs/bin/_internal/static/`. Este arquivo permite definir os campos do formulário seguindo uma estrutura predefinida.

##### Estrutura do form.json

Para gerar um formulário corretamente a partir de um arquivo form.json, é necessário respeitar a seguinte estrutura:

```json
{
    "title": "Formulário de exemplo",
    "inputs": [
        {
            "type": "input",
            "title": "Digite seu nome",
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

O arquivo form.json é processado pelo ProbeForms para gerar um formulário HTML no arquivo index.html. Os campos do formulário são definidos no array `inputs`, onde cada objeto representa um campo. O objeto `submit` define o botão de envio.

##### Detalhes dos campos do formulário

- **title**: Título do formulário

- **inputs**: As diferentes entradas de informação que o usuário poderá preencher. As opções disponíveis e seus diferentes campos são os seguintes:
    - **type**: Indica o tipo de entrada a ser usada no formulário. Opções disponíveis: label, input, select, select, checkbox, textarea, radio
    - **title**: Título da entrada.
    - **id**: Identificador único da entrada. Não deve ser duplicado, pois corresponde à chave do json no resultado retornado.
    - **format**: Disponível apenas em entradas de tipo input. Suas opções são text, password, email.
    - **column-class**: Classe css do Bootstrap que terá o contêiner de entrada. Por padrão, col-md-12
    - **css**: Classes css do Bootstrap que a entrada terá.
    - **required**: Indica se a entrada é obrigatória. Padrão falso

- **submit**: Esta seção permite modificar o texto e o estilo do botão que envia o formulário. As opções disponíveis são as seguintes:
    - **title**: Texto que o botão terá.
    - **css**: Classes css do Bootstrap que darão o estilo desejado ao botão.

> 💡 **Nota**: Se um arquivo `form.json` for usado para gerar o formulário, o conteúdo do arquivo `index.html` será substituído em cada execução do módulo. É recomendável salvar uma cópia de `index.html` se os testes estiverem em andamento.

### Geração e Uso do Formulário

Uma vez definido o arquivo form.json, o formulário pode ser gerado e exibido executando o módulo ProbeForms. Isso iniciará o serviço local e abrirá o formulário no navegador padrão.

#### Recebimento de dados

Quando o formulário é enviado, os dados serão armazenados na memória enquanto o ProbeForms estiver em execução. Esses dados podem ser recuperados usando o comando Aguardar por Mensagem em um modelo FIFO (First In First Out). Se não houver dados disponíveis em uma solicitação GET, a solicitação permanecerá pendente até que os dados sejam concluídos ou o tempo limite definido seja atingido.