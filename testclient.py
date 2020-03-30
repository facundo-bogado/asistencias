import requests
import json
#from functools import reduce
from generador import *

r=requests.post(
    "http://127.0.0.1:4000/registrar_alumno",
    headers={"Content-Type":"application/json"},
    data=json.dumps(
        {
            "nombre":"marcos",
            "dni":34567234,
            "hardware":"jbijiem685",
            "nick":"mark",
            "password":"kjiguyf"
        }))
print(r.text)

print(requests.get(
    "http://127.0.0.1:4000/listado_alumnos").text)