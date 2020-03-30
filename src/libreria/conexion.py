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