from app import db, ma

class Clients(db.Model):
    client_id = db.Column(db.Integer, primary_key = True)
    client_name = db.Column(db.String(50), nullable = False)
    client_last_name = db.Column(db.String(50), nullable = False)
    client_email = db.Column(db.String(50), nullable = False)
    client_password = db.Column(db.String(50), nullable = False)
    client_contact = db.Column(db.Integer, nullable = False)

    def __init__(self, client_name, client_last_name, client_email, client_password, client_contact):
        self.client_name = client_name
        self.client_last_name = client_last_name
        self.client_email = client_email
        self.client_password = client_password
        self.client_contact = client_contact
    
# db.create.all()

class ClientSchema(ma.Schema):
    class Meta:
        fields = ("client_id", "client_name", "client_last_name", "client_email", "client_password", "client_contact")

client_schema = ClientSchema()
clients_schema = ClientSchema(many = True)