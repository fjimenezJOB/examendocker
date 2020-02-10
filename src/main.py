from flask import Flask, render_template, redirect, url_for, request, session
import os
from libreria.conexion import *

app = Flask(__name__)

app.secret_key = 'esto-es-una-clave-muy-secreta'

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        print(nombre)
        session['nombre'] = nombre
        session['email'] = email
        error = insertarParticipante(nombre, email)
        if error:
            return render_template('index.html', error = error)

    participantes = sacarParticipantes()
    context = { 
        'titulo': 'Bienvenido !!',
        'subtitulo': 'Solo tienes que registrar tu Nombre y tu correo electronico para participar.',
        'participantes' : participantes
    }
    return render_template('index.html', **context)

@app.route('/home')
def home():
    context = {
        'titulo' : 'Bienvenido al sorteo ' + session['nombre'],
        'subtitulo' : 'Estas registrado como ' + session['email']
    }
    return render_template('home.html', **context )
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port, debug=True)
