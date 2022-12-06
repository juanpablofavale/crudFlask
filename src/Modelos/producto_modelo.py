from app import db, ma, app

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    tamanio = db.Column(db.String(100))
    precio = db.Column(db.Float)
    hoja = db.Column(db.Integer)
    plato = db.Column(db.Integer)
    subtipo = db.Column(db.Integer)

    def __init__(self, nombre, tamanio, precio, hoja, plato, subtipo):
        self.nombre=nombre
        self.tamanio=tamanio
        self.precio=precio
        self.hoja=hoja
        self.plato=plato
        self.subtipo=subtipo

with app.app_context():
    db.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id', 'nombre', 'tamanio', 'precio', 'hoja', 'plato', 'subtipo')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
