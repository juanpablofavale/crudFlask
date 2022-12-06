from app import *
from Modelos.subtipo_modelo import *

@app.route('/subtipos', methods=['GET'])
def get_subtipos():
    all_subtipos = Subtipo.query.all()
    result = subtipos_schema.dump(all_subtipos)
    return jsonify(result)

@app.route('/subtipos/<id>', methods=['GET'])
def get_subtipo(id):
    subtipo = Subtipo.query.get(id)
    result = subtipo_schema.dump(subtipo)
    return jsonify(result)

@app.route('/subtipos', methods=['POST'])
def create_subtipo():
    new_subtipo = Subtipo(request.json['nombre'])
    db.session.add(new_subtipo)
    db.session.commit()
    return subtipo_schema.jsonify(new_subtipo)

@app.route('/subtipos/<id>', methods=['PUT'])
def update_subtipo(id):
    subtipo = Subtipo.query.get(id)
    subtipo.nombre = request.json['nombre']
    db.session.commit()
    return subtipo_schema.jsonify(subtipo)

@app.route('/subtipos/<id>', methods=['DELETE'])
def delete_subtipo(id):
    subtipo = Subtipo.query.get(id)
    db.session.delete(subtipo)
    db.session.commit()
    return subtipo_schema.jsonify(subtipo)
