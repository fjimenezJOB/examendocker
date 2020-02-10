from pymongo import MongoClient
from flask import session
import time


MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs = False)

db = client['sorteoweb']

collection = db['participantes']

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

insertarParticipante('Fran Jimenez', 'franloloco@gmail.com')