from app import db, ma, app

class Usuario(db.Model):
    user = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(50))
    activo = db.Column(db.Integer)

    def __init__(self, user, password, activo = 0):
        self.user=user
        self.password=password
        self.activo=activo

with app.app_context():
    db.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('user', 'password', 'activo')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
