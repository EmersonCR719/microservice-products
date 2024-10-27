from flask import Flask, jsonify, request
import mysql.connector
from config import Config
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Permite solicitudes desde el frontend (CORS)

def get_connection():
    return mysql.connector.connect(
        host = Config.HOST,
        port = Config.PORT,
        user = Config.USER,
        password = Config.PASSWORD,
        database = Config.DATABASE)


@app.route('/productos', methods=['GET'])
def get_productos():
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * from producto")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return jsonify(productos), 200

@app.route('/productos/<int:id>', methods=['GET'])
def get_producto_x_id(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * from producto where id = %s", (id,) )
    producto = cursor.fetchone()
    cursor.close()
    conexion.close()

    if producto:
        return jsonify(producto), 200
    return jsonify({"mensaje": "No se encontro"}), 404



@app.route('/productos', methods=['POST'])
def post_productos():
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO producto (nombre, categoria, cantidad, fecha_adquisicion) VALUES(%s, %s, %s, %s);"
    cursor.execute(sql , (request.json['nombre'],request.json['categoria'], request.json['cantidad'],
                    request.json['fecha_adquisicion']) )
    conexion.commit()
    id_new = cursor.lastrowid
    cursor.close()
    conexion.close()  

    return jsonify( {'id':id_new}), 201

@app.route('/productos/<int:id>', methods=['PUT'])
def put_productos(id):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE producto SET nombre = %s, categoria = %s, cantidad =%s, fecha_adquisicion = %s WHERE id = %s"
    cursor.execute(sql , (request.json['nombre'],request.json['categoria'], request.json['cantidad'],
                    request.json['fecha_adquisicion'],id) )
    conexion.commit()

    cursor.close()
    conexion.close()  

    return jsonify({"id": id}), 200



@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto_x_id(id):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM producto WHERE id = %s"
    cursor.execute(sql , (id,) )
    conexion.commit()

    cursor.close()
    conexion.close()  
    return jsonify({"mensaje": "Producto eliminado"}), 200


if __name__ == '__main__':
    app.run(debug=True, port="3000")