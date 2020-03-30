import os
import time
from hashlib import sha256
import json

pcId=lambda:list(filter(lambda x:x[0:16]=="Id. del producto",os.popen("systeminfo").readlines()))[0].split(" ")[-1][0:-1]
sha_it=lambda data: sha256(data.encode()).hexdigest()

def registro_form(nombre,dni,nick,passw):
    return json.dumps(
        {
            "nombre":nombre,
            "dni":dni,
            "hardware":pcId(),
            "nick":nick,
            "password":sha_it(passw)
        })

def asistencia(dni,nick,password):
	return json.dumps(
		{
			"dni":dni,
			"nick":nick,
			"password":sha_it(password),
			"hardware":pcId()
		})

if __name__=="__main__":
    print(sha_it("tincho"))
