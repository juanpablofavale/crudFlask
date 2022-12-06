from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/rotibuenavoluntad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

from Controladores.plato_controlador import *
from Controladores.subtipo_controlador import *
from Controladores.producto_controlador import *
from Controladores.usuario_controlador import *

#Aplicacion Principal

if __name__ == '__main__':
    app.run(debug=True, port=5000)
