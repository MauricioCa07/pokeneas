from flask import Blueprint, jsonify, render_template
import random
import socket

bp = Blueprint('routes', __name__)

POKENEAS = [
    {"id": 1, "nombre": "Pokenea1", "altura": "1.2m", "habilidad": "Rayo Solar", "imagen": "https://storage.googleapis.com/pokedea-images/001.png", "frase": "La vida es un rayo fugaz."},
    {"id": 2, "nombre": "Pokenea2", "altura": "1.5m", "habilidad": "Puño Fuego", "imagen": "https://storage.googleapis.com/pokedea-images/002.png", "frase": "El fuego es la chispa que ilumina el alma."},
    {"id": 3, "nombre": "Pokenea3", "altura": "1.3m", "habilidad": "Tormenta de Arena", "imagen": "https://storage.googleapis.com/pokedea-images/003.png", "frase": "Las tormentas nos enseñan a resistir."},
    {"id": 4, "nombre": "Pokenea4", "altura": "1.0m", "habilidad": "Destello", "imagen": "https://storage.googleapis.com/pokedea-images/004.png", "frase": "El brillo de la verdad es más fuerte que cualquier oscuridad."},
    {"id": 5, "nombre": "Pokenea5", "altura": "1.7m", "habilidad": "Hidrochorro", "imagen": "https://storage.googleapis.com/pokedea-images/005.png", "frase": "El agua siempre encuentra su camino."},
    {"id": 6, "nombre": "Pokenea6", "altura": "1.4m", "habilidad": "Puño Bala", "imagen": "https://storage.googleapis.com/pokedea-images/006.png", "frase": "La fuerza interior es la clave del éxito."},
    {"id": 7, "nombre": "Pokenea7", "altura": "1.2m", "habilidad": "Corte Aéreo", "imagen": "https://storage.googleapis.com/pokedea-images/007.png", "frase": "Vuela alto, sueña en grande."},
    {"id": 8, "nombre": "Pokenea8", "altura": "1.6m", "habilidad": "Pulso de Energía", "imagen": "https://storage.googleapis.com/pokedea-images/008.png", "frase": "La energía que damos al mundo regresa multiplicada."},
    {"id": 9, "nombre": "Pokenea9", "altura": "1.1m", "habilidad": "Llama Eterna", "imagen": "https://storage.googleapis.com/pokedea-images/009.png", "frase": "Las llamas nunca se apagan si sigues avivándolas."},
    {"id": 10, "nombre": "Pokenea10", "altura": "1.8m", "habilidad": "Puño Trueno", "imagen": "https://storage.googleapis.com/pokedea-images/010.png", "frase": "La fuerza del trueno resuena en nuestros corazones."}
]


@bp.route('/api/random', methods=['GET'])
def api_random():
    pokenea = random.choice(POKENEAS)
    contenedor_id = socket.gethostname()
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": contenedor_id
    })

@bp.route('/pokenea', methods=['GET'])
def show_pokenea():
    pokenea = random.choice(POKENEAS)
    contenedor_id = socket.gethostname()
    return render_template('pokenea.html', pokenea=pokenea, contenedor_id=contenedor_id)
