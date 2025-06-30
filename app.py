#Aquí se presenta un backend muy minimalista con Flask que expone un único endpoint GET.
#Este backend simula tener una lista de "mensajes" almacenados que puede entregar cuando se le solicitan.

from flask import Flask, jsonify

app = Flask(__name__)

# --- Base de Datos en Memoria para este ejemplo ---
# Una lista simple de diccionarios que simula nuestros datos.
mensajes_disponibles = [
    {"id": 1, "texto": "Hola desde la API de Flask!"},
    {"id": 2, "texto": "Este es el segundo mensaje."},
    {"id": 3, "texto": "Aprendiendo APIs GET."}
]

# --- Ruta para el método GET ---
# Define un endpoint que responde a solicitudes GET en /api/mensajes
@app.route('/api/mensajes', methods=['GET'])
def get_all_messages():
    """
    Retorna todos los mensajes disponibles como una respuesta JSON.
    """
    print("Solicitud GET recibida en /api/mensajes")  # Para ver en la terminal
    return jsonify(mensajes_disponibles)  # Convierte la lista Python a formato JSON

# --- Punto de entrada para ejecutar la aplicación Flask ---
if __name__ == '__main__':
    # Inicia el servidor Flask en modo depuración.
    # debug=True permite recarga automática y un depurador básico.
    app.run(debug=True)