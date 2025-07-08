from flask import Flask, request, jsonify
import sqlite3
import bcrypt
import os

app = Flask(__name__)

DB_FILE = 'usuarios_login.db'

# Crea BD y Tabla en Caso de NO Existir
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            contrasena_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Agrega Nuevo Usuario c/ Clave HASH
def agregar_usuario(nombre, contrasena):
    contrasena_hash = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, contrasena_hash) VALUES (?, ?)", (nombre, contrasena_hash))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Verifica Inicio de Sesión (login)
def verificar_usuario(nombre, contrasena):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT contrasena_hash FROM usuarios WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return bcrypt.checkpw(contrasena.encode('utf-8'), resultado[0])
    return False

# Ruta Registro de Usuario
@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    if nombre and contrasena:
        if agregar_usuario(nombre, contrasena):
            return jsonify({'mensaje': 'Usuario registrado correctamente.'}), 201
        else:
            return jsonify({'error': 'Usuario ya existe.'}), 400
    return jsonify({'error': 'Datos incompletos.'}), 400

# Ruta Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    if verificar_usuario(nombre, contrasena):
        return jsonify({'mensaje': 'Login exitoso.'})
    return jsonify({'error': 'Credenciales inválidas.'}), 401

@app.route("/")
def home():
    return "Servidor operando sin problemas."

# Ejecuta el Server c/ Puerto 5800
if __name__ == '__main__':
    init_db()
    app.run(host="127.0.0.1", port=5800)