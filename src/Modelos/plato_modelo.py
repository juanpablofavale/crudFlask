from app import db, ma, app

class Plato(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))

    def __init__(self, nombre):
        self.nombre=nombre

with app.app_context():
    db.create_all()

class PlatoSchema(ma.Schema):
    class Meta():
        fields=('id', 'nombre')

plato_schema = PlatoSchema()
platos_schema = PlatoSchema(many=True)
