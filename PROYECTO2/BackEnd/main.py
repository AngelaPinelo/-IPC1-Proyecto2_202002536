from flask import Flask, request, jsonify, redirect
from flask_cors import CORS 

import json 

app = Flask (__name__)

Usuarios1 =[]
CORS (app)
#Actividad 1---------------------------------------------------------------------------------------------
@app.route ("/login", methods=['POST'])
def ingresarusuario():
    user = (request.json['usuario'])
    password = (request.json['password'])
    respuesta = jsonify ({"error": False, "mensaje": "Todo bien", "usuario":"normal"})
    return (respuesta)


vocales = 0


def es_vocal(frase): 
    global vocales 
    vocales = 0
    fraseMinusculas = frase.lower()
    for letra in fraseMinusculas: 
        if ord (letra) == 97 or ord (letra) == 101 or ord (letra) == 105 or ord (letra) == 111 or ord (letra) == 117:
            vocales+=1 
    print(vocales)

#Fin actividad1-------------------------------------------------------------------------------------

#Actividad 2----------------------------------------------------------------------------------------
@app.route ("/numeros", methods=['POST'])
def numeros():
    global primos
    primos=0 
    numero1 = int(request.json['inferior'])
    numero2 = int(request.json['superior'])
    for i in range (numero1,numero2+1):
        primos1(i)
    respuesta = jsonify ({"error": False, "mensaje": "Todo bien"})
    return (respuesta)
primos = 0
def primos1(num): 
    global primos

    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                primos += 1
                             

@app.route("/numeros", methods = ['GET'])
def obtenernumeros():
    global primos
    envios= []
    unEnvio= {
            "primos": primos,
        }
    envios.append(unEnvio)
    respuesta = jsonify(envios)
    return respuesta
#Fin actividad 2------------------------------------------------------------------------------
#Actividad 3----------------------------------------------------------------
@app.route ("/calculadora", methods=['POST'])
def calc():
    print("funciona")
    numero1 = int(request.json['numero1'])
    numero2 = int(request.json['numero2'])
    signo = request.json ['signo']
    calculo(numero1, numero2, signo)
    respuesta = jsonify ({"error": False, "mensaje": "Todo bien"})
    return (respuesta)
resultado  = 0
def calculo(numero1,numero2,signo): 
    global resultado
    resultado = 0
    if ord (signo)   == 42 : 
        resultado = numero1 * numero2
    if ord (signo) == 43:
        resultado = numero1 + numero2
    if ord (signo) == 45:
        resultado = numero1 - numero2
    if ord (signo) == 47:
        resultado = numero1/numero2 


@app.route("/calculo", methods = ['GET'])
def tomatera():
    global resultado
    envios= []
    unEnvio= {
            "resultado": resultado,
        }
    envios.append(unEnvio)
    respuesta = jsonify(envios)
    return respuesta

if __name__ == "__main__":
    app.run(host="0.0.0.0", port =4000, debug=True)