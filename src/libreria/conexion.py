from pymongo import MongoClient
from flask import session
import datetime
import time
import calendar
import random


MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs = False)
db = client['sorteoweb']
contador = None

def insertarParticipante(nombre, email):
    collection = db['participantes']
    """
        Inserta los participantes en la base de datos. ( Nombre de participante, correo electronico y la fecha actual. )
    """
    resultados = collection.find({'email': email}, {'_id': 0, 'email': 1, 'activo': 1})

    lista = []
    for documento in resultados:
        lista.append(documento)
    
    for documento in lista:
        if email == documento['email']:
            error = True
            return error

    fecha = datetime.datetime.now()
    collection.insert_one({'nombre': nombre, 'email': email, 'fecha': fecha ,'activo' : 1})

def sacarParticipantes():
    collection = db['participantes']
    resultados = collection.find({},{'_id': 0, 'nombre': 1, 'activo': 1, 'fecha': 1 })
    listaParticipantes = []
    for documento in resultados:
        if documento['activo'] == 1:
            listaParticipantes.append(documento)
    return listaParticipantes


def sacarPremios():
    collection = db['premios']
    lista = []
    resultados = collection.find({'activo':1}, {'premio':1})
    for i in resultados:
        lista.append(i)
    return lista

def subirFecha(fecha):
    collection = db['fechaSorteo']
    collection.replace_one({}, {'sorteo': fecha})

def recogerFecha():
    fecha = None
    collection = db['fechaSorteo']
    fecha_dic = collection.find({},{'sorteo':1})
    for fechas in fecha_dic:
        fecha = fechas['sorteo']
    return fecha


def logicaFecha():
    fechaSorteo = recogerFecha()
    fechaSeparada = fechaSorteo.split('/', 3)
    fecha_hoy = datetime.datetime.now()
    dia_hoy = fecha_hoy.day
    fecha_x = datetime.datetime(int(fechaSeparada[0]),int(fechaSeparada[1]),int(fechaSeparada[2]))
    resultado = fecha_hoy - fecha_x
    return str(resultado.days)
