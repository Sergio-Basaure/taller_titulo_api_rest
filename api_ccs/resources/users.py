from app import db, ma


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_nick = db.Column(db.String(50), nullable = True)
    user_name = db.Column(db.String(50), nullable = False)
    user_last_name = db.Column(db.String(50), nullable = False)
    user_password = db.Column(db.String(50), nullable = False)
    user_email = db.Column(db.String(50), nullable = False)
    user_contact = db.Column(db.Integer, nullable = False)
    user_job = db.Column(db.String(20), nullable = False)

    def __init__(self, user_name,user_nick, user_last_name, user_password, user_email, user_contact, user_job):
        self.user_name = user_name
        self.user_nick = user_nick
        self.user_last_name = user_last_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_contact = user_contact
        self.user_job = user_job

# db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "user_nick", "user_name", "user_last_name", "user_password", "user_email", "user_contact", "user_job")

user_schema = UserSchema()
users_schema = UserSchema(many = True)
