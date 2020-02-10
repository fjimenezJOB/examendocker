from pymongo import MongoClient
from flask import session
import datetime
import time
import calendar
import random


MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs = False)

db = client['sorteoweb']

collection = db['participantes']

contador = None

def insertarParticipante(nombre, email):
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

    fecha = time.strftime("%d/%m/%y")
    print (fecha)
    collection.insert_one({'nombre': nombre, 'email': email, 'fecha': fecha ,'activo' : 1})

def sacarParticipantes():
    resultados = collection.find({},{'_id': 0, 'nombre': 1, 'activo': 1, 'fecha': 1 })

    listaParticipantes = []
    for documento in resultados:
        if documento['activo'] == 1:
            listaParticipantes.append(documento)
    return listaParticipantes

collection = db['premios']

def introducirPremios():
    fecha = time.strftime("%d/%m/%y")
    collection.insert_one({'premio':'Gafas de sol Ray Ban estilo aviador','fecha':fecha, 'activo': 1})

def sacarPremios():
    fecha = time.strftime("%d/%m/%y")
    fechaCortada = fecha.split('/', 2)
    fechaAdate = datetime.date(int(fechaCortada[2]),int(fechaCortada[1]), int(fechaCortada[0]))
    wk = fechaAdate.isocalendar()[1]
    
    resultados = collection.find({'activo':1}, {'premio':1})
