# ProbeForms
  
Module to generate offline forms and send the information to Rocketbot  

*Read this in other languages: [English](Manual_ProbeForms.md), [Português](Manual_ProbeForms.pr.md), [Español](Manual_ProbeForms.es.md)*
  
![banner](imgs/Banner_ProbeForms.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## How to use this module

ProbeForms is a tool that allows you to create forms to collect information from users.

### How it works

When you download the ProbeForms module, it includes an executable that starts a local server to serve the form. The executable is located in the `Rocketbot/modules/ProbeForms/libs/bin` folder.

There are two methods for editing the form fields.

#### Method 1 (Recommended)

Inside the module folder, in `libs/bin/_internal/static/` you will find the index.html file, which presents the form visually. This file allows you to directly edit the content inside the `<form action="/submit" method="post" id="probeForm">` tag, where you can customize the fields according to your needs. The information is sent to the corresponding endpoint through the `<script>` tag. It is recommended that you do not modify this script to ensure that the data is sent correctly. Inside the `<script>` tag are also the functions that run in the ProbeForms service to get the path of 
files and folders. It is recommended that you do not modify them to ensure the correct operation of the module.

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


## Description of the commands

### Run ProbeForms
  
This command allows you to run the ProbeForms service.
|Parameters|Description|example|
| --- | --- | --- |
|Port|Port where the ProbeForms service will run|4321|

### Wait submit
  
This command allows you to wait for a ProbeForms form to be submitted.
|Parameters|Description|example|
| --- | --- | --- |
|Maximum waiting time (seconds)|Maximum time the robot will wait for a message|3600|
|Port|Port where the ProbeForms service will run|4321|
|Assign result to variable|Name of the variable of your robot that will store the result of the form|variable|

### Close ProbeForms
  
This command allows you to close the ProbeForms service.
|Parameters|Description|example|
| --- | --- | --- |
