from app import db, ma, app

class Subtipo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))

    def __init__(self, nombre):
        self.nombre=nombre

with app.app_context():
    db.create_all()

class SubtipoSchema(ma.Schema):
    class Meta():
        fields=('id', 'nombre')

subtipo_schema = SubtipoSchema()
subtipos_schema = SubtipoSchema(many=True)
