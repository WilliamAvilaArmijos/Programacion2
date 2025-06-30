from flask import Flask, request, jsonify
import jwt
import datetime
import sqlite3
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Usar variable de entorno para la clave secreta
SECRET_KEY = os.getenv("SECRET_KEY", "mi_clave_secreta")

# Crear base de datos y usuarios por defecto
def crear_bd():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Insertar usuarios de prueba
    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", ("carolina", "1234"))
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", ("admin", "admin"))
    except sqlite3.IntegrityError:
        pass  # Los usuarios ya existen
    conn.commit()
    conn.close()

crear_bd()

# Login → genera token
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    username = datos.get('username')
    password = datos.get('password')

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE username=?", (username,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and resultado[0] == password:
        token = jwt.encode({
            "usuario": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token}), 200
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401

# Ruta protegida con verificación del token
@app.route('/protegido', methods=['GET'])
def protegido():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"mensaje": "Token no proporcionado"}), 401

    token = auth_header.split(" ")[-1]  # Soporta "Bearer <token>" o solo el token

    try:
        datos = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"mensaje": f"Hola {datos['usuario']}, accediste con tu token."})
    except jwt.ExpiredSignatureError:
        return jsonify({"mensaje": "Token expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"mensaje": "Token inválido"}), 401

if __name__ == '__main__':
    app.run(debug=True)