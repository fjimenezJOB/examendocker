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
        session['nombre'] = nombre
        session['email'] = email
        error = insertarParticipante(nombre, email)

        if error:
            return render_template('index.html', error = error)

    participantes = sacarParticipantes()
    premios = sacarPremios()
    diasRestantes = logicaFecha()

    if diasRestantes == "0":
        numeroRandom = random.randrange(0,len(premios))
        randomPremiado = random.randrange(0, len(participantes))
        premiado = participantes[randomPremiado]
        premio = premios[numeroRandom]

        context = { 
            'titulo': 'Bienvenido !!',
            'subtitulo': 'Solo tienes que registrar tu Nombre y tu correo electronico para participar.',
            'participantes' : participantes,
            'premios' : premios,
            'diasRestantes' : diasRestantes,
            'premio': premio['premio'],
            'premiado' : premiado['nombre']
        }
    else:
        context = { 
            'titulo': 'Bienvenido !!',
            'subtitulo': 'Solo tienes que registrar tu Nombre y tu correo electronico para participar.',
            'participantes' : participantes,
            'premios' : premios,
            'diasRestantes' : diasRestantes
        }

    return render_template('index.html', **context)

@app.route('/admin', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        nuevaFecha = request.form.get('fecha')
        print(nuevaFecha)
        subirFecha(nuevaFecha)
    context = {
        'titulo' : 'Bienvenido Admin'
    }
    return render_template('admin.html', **context )
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port, debug=True)
