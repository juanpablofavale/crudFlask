from app import *
from Modelos.usuario_modelo import *

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)
    return jsonify(result)

@app.route('/usuarios/<user>', methods=['GET'])
def get_usuario(user):
    usuario = Usuario.query.get(user)
    result = usuario_schema.dump(usuario)
    return jsonify(result)

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    user = request.json['user']
    password = request.json['password']
    activo = request.json['activo']
    new_usuario = Usuario(user, password, activo)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

@app.route('/usuarios/<user>', methods=['PUT'])
def update_usuario(user):
    usuario = Usuario.query.get(user)
    usuario.user = request.json['user']
    usuario.password = request.json['password']
    usuario.activo = request.json['activo']
    db.session.commit()
    return usuario_schema.jsonify(usuario)

@app.route('/usuarios/<user>', methods=['DELETE'])
def delete_usuario(user):
    usuario = Usuario.query.get(user)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)