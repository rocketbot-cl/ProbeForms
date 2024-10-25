# ProbeForms
  
Módulo para gerar formulários offline e enviar as informações para Rocketbot  

*Read this in other languages: [English](Manual_ProbeForms.md), [Português](Manual_ProbeForms.pr.md), [Español](Manual_ProbeForms.es.md)*
  
![banner](imgs/Banner_ProbeForms.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo

ProbeForms é uma ferramenta que permite criar formulários para coletar informações dos usuários.

### Como funciona

Ao baixar o módulo ProbeForms, ele inclui um executável que inicia um servidor local para servir o formulário. O executável está localizado na pasta `Rocketbot/modules/ProbeForms/libs/bin`.

Existem dois métodos para editar os campos do formulário.

#### Método 1 (Recomendado)

Dentro da pasta do módulo, em `libs/bin/_internal/static/`, você encontrará o arquivo index.html, que apresenta o formulário visualmente. Este arquivo permite que você edite diretamente o conteúdo dentro da tag `<form action="/submit" method="post" id="probeForm">`, onde você pode personalizar os campos de acordo com suas necessidades. As informações são enviadas para o endpoint correspondente através da tag `<script>`. Recomenda-se não modificar este script para garantir que os dados sejam enviados corretamente. Dentro da tag `<script>` também estão as funções que são 
executadas no serviço ProbeForms para obter o caminho de arquivos e pastas. Recomenda-se não modificá-las para garantir o correto funcionamento do módulo.

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

Quando o formulário é enviado, os dados serão armazenados na memória enquanto o ProbeForms estiver em execução. Esses dados podem ser recuperados usando o comando Aguardar por Mensagem em um modelo FIFO (First In First Out). Se não 
houver dados disponíveis em uma solicitação GET, a solicitação permanecerá pendente até que os dados sejam concluídos ou o tempo limite definido seja atingido.
## Descrição do comando

### Executar ProbeForms
  
Este comando permite executar o serviço de ProbeForms.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Porta|Porta onde o serviço ProbeForms será executado|4321|

### Aguardar envio
  
Este comando permite aguardar um formulário de ProbeForms ser enviado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tempo máximo de espera (segundos)|Tempo máximo que o robô aguardará por uma mensagem|3600|
|Porta|Porta onde o serviço ProbeForms será executado|4321|
|Atribuir resultado à variável|Nome da variável do seu robô que armazenará o resultado do formulário|variable|

### Fechar ProbeForms
  
Este comando permite fechar o serviço de ProbeForms.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
