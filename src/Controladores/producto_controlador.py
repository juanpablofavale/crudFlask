from app import *
from Modelos.producto_modelo import *

@app.route('/productos', methods=['GET'])
def get_productos():
    all_productos = Producto.query.all()
    result = productos_schema.dump(all_productos)
    return jsonify(result)

@app.route('/productos/<id>', methods=['GET'])
def get_producto(id):
    prod = Producto.query.get(id)
    result = producto_schema.dump(prod)
    return jsonify(result)

@app.route('/productos', methods=['POST'])
def create_producto():
    print(request.json)
    nombre = request.json['nombre']
    tamanio = request.json['tamanio']
    precio = request.json['precio']
    hoja = request.json['hoja']
    plato = request.json['plato']
    subtipo = request.json['subtipo']
    new_producto = Producto(nombre, tamanio, precio, hoja, plato, subtipo)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<id>', methods=['PUT'])
def update_producto(id):
    prod = Producto.query.get(id)

    prod.nombre = request.json['nombre']
    prod.tamanio = request.json['tamanio']
    prod.precio = request.json['precio']
    prod.hoja = request.json['hoja']
    prod.plato = request.json['plato']
    prod.subtipo = request.json['subtipo']

    db.session.commit()
    return producto_schema.jsonify(prod)

@app.route('/productos/<id>', methods=['DELETE'])
def delete_producto(id):
    prod = Producto.query.get(id)
    db.session.delete(prod)
    db.session.commit()
    return producto_schema.jsonify(prod)
