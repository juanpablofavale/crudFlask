from app import *
from Modelos.plato_modelo import *

@app.route('/platos', methods=['GET'])
def get_platos():
    all_platos = Plato.query.all()
    result = platos_schema.dump(all_platos)
    return jsonify(result)

@app.route('/platos/<id>', methods=['GET'])
def get_plato(id):
    plato = Plato.query.get(id)
    result = plato_schema.dump(plato)
    return jsonify(result)

@app.route('/platos', methods=['POST'])
def create_plato():
    new_plato = Plato(request.json['nombre'])
    db.session.add(new_plato)
    db.session.commit()
    return plato_schema.jsonify(new_plato)

@app.route('/platos/<id>', methods=['PUT'])
def update_plato(id):
    plato = Plato.query.get(id)
    plato.nombre = request.json['nombre']
    db.session.commit()
    return plato_schema.jsonify(plato)

@app.route('/platos/<id>', methods=['DELETE'])
def delete_plato(id):
    plato = Plato.query.get(id)
    db.session.delete(plato)
    db.session.commit()
    return plato_schema.jsonify(plato)
