# coding=utf-8
from flask import Flask, request, jsonify
import time
from functools import reduce
from pdb import  dbalumnos, presentes
#import sqlite3


app=Flask(__name__)


@app.route("/listado_alumnos")
def listar_alumnos():
    return jsonify({k:v["nombre"]+" - "+v["nick"] for k,v in dbalumnos.items()})


@app.route("/registrar_alumno", methods=["POST"])
def registrar_alumno():
    keys_in=lambda ks,db:map(lambda x:x in db,ks)
    if reduce(lambda a,x:a and x,keys_in(("nombre","dni","hardware","nick","password"),request.json)):
        dbalumnos[request.json["dni"]]=request.json
        print(dbalumnos)
        with open("pdb.py","w") as db:
            db.write("dbalumnos="+str(dbalumnos)+"\n"+"presentes="+str(presentes))
        return jsonify({
            "status":"Se registro el alumno con exito!",
            "alumno":request.json["nombre"]+" - "+str(request.json["dni"])})
    else:
        return jsonify({
            "status":"No se pudo agregar los datos",
            "tip":"revise los datos, podrian faltar o ser inválidos."})


@app.route("/listado_presentes")
def listar_presentes():
    return jsonify(presentes)


@app.route("/registrar_asistencia", methods=["POST"])
def registrar_asistencia():
    dni=int(request.json["dni"])
    if dni in dbalumnos:
        if dbalumnos[dni]["nick"]==request.json["nick"] and dbalumnos[dni]["password"]==request.json["password"]:
            if dbalumnos[dni]["hardware"]==request.json["hardware"]:
                presentes[dni]=request.json["nombre"]
                return jsonify({
                    "status":"Su asistencia se registró con éxito",
                    "alumno":request.json["nombre"]+" - "+str(dni)})
            else:
                return jsonify({
                    "status":"no se pudo completar el registro",
                    "tip":"El hardware usado no corresponde al registrado, consulte a la preceptora."
                    })
        else:
            return jsonify({
                "status":"No se ha podido completar el registro",
                "tip":"nick, password incorrectos."
                })
    else:
        return jsonify({
            "status":"No se ha podido completar el registro",
            "tip":"DNI no registrado o mal ingresado."})


if __name__=="__main__":
    app.run(debug=True, port=4000)
