from pymongo import MongoClient
from flask import session
import datetime


MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs = False)

db = client['sorteoweb']

collection = db['participantes']

def insertarParticipante(nombre, email):
    """
        Inserta los participantes en la base de datos. ( Nombre de participante, correo electronico y la fecha actual. )
    """
    fecha = datetime.date.today()
    print (fecha)
    collection.insert_one({'nombre': nombre, 'email': email, 'fecha': fecha ,'activo' : 1})