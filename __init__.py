# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys
import traceback
import subprocess

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'ProbeForms' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import probe_requests as requests # type: ignore
from probe_requests.exceptions import Timeout, ConnectionError # type: ignore


global mod_processProbeForms

module = GetParams("module")

try:
    if module == "run_probeforms":
        port = GetParams("port")

        try:
            mod_processProbeForms = subprocess.Popen([f"{cur_path}bin{os.sep}probeforms.exe", "--port", port])

            try:
                webbrowser.get('chrome').open(f"http://localhost:{port}")
            

            except Exception as e:
                webbrowser.open(f"http://localhost:{port}")
            

        except Exception as e:
            PrintException()
            raise e
       
    if module == "wait_message":
        timeout = int(GetParams("timeout")) if GetParams("timeout") else 3600
        result = GetParams("result")
        port = GetParams("port")

        try:
            data = requests.get(f"http://localhost:{port}/message", timeout=timeout)
            
            data = data.json()

            SetVar(result, data["data"])
        except ConnectionError:
            SetVar(result, "Connection error.")
            raise Exception("Connection error. Please make sure ProbeForms is running.")
        except Timeout:
            SetVar(result, "The request timed out.")
            raise Exception("The request timed out.")
        except Exception as e:
            PrintException()
            raise e

    if module == "close_probeforms":
        if mod_processProbeForms:
            mod_processProbeForms.terminate()
            mod_processProbeForms = None
        else:
            raise Exception("ProbeForms is not running.")

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e