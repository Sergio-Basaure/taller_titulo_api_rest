from flask import jsonify, request
from app import app, db
from api_ccs.resources.users import *
from api_ccs.resources.clients import *

message_succsess = {
    'message' : 'success'
}
message_error = {
    'message' : 'fail'
}

@app.route('/add-user', methods = ['POST'])
def new_user():
    if request.json != None:
        user_name = request.json['user_name']
        user_last_name = request.json['user_last_name']
        user_password = request.json['user_password']
        user_email = request.json['user_email']
        user_contact = request.json['user_contact']

        new_user = Users(user_name, user_last_name, user_password, user_email, user_contact)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message_succsess)
    else:
        return jsonify(message_error)



@app.route('/get_users')
def get_users():
    users = Users.query.all()
    all_users = users_schema.dump(users)
    return jsonify(all_users)

# agregar metodo para traer usuario con el nick

@app.route('/get_user/<int:user_id>')
def get_user(user_id):
    user = Users.query.get(user_id)
    return user_schema.jsonify(user)

@app.route('/update_user/<int:user_id>', methods = ['PUT'])
def update_user(user_id):
    user_id = Users.query.get(user_id)
    # ver que se va a modificar

@app.route('/delete_user/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    user = Users.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(message_succsess)


# @app.route('/add_client', methods = ['POST'])
# def add_client():
#     if request.json != None:
#         client_name = request.json['client_name']
#         client_last_name = request.json['client_last_name']
#         client_email = request.json['client_email']
#         client_password = request.json['client_password']
#         client_contact = request.json['client_contact']
#         new_client = Clients(client_name, client_last_name, client_email, client_password, client_contact)
#         db.session.add(new_client)
#         db.session.commit()
#         return jsonify(message_succsess)
#     else:
#         return jsonify(message_error)


# @app.route('/get_clients')
# def get_clients():
#     clients = Clients.query.all()
#     return clients_schema.jsonify(clients)


# @app.route('/get_client/<int:client_id>')
# def get_client(client_id):
#     client = Clients.query.get(client_id)
#     return client_schema.jsonify(client)

# # ver metodo para traer a cliente que no sea por id

# @app.route('/update_client/<int:client_id>', methods = ['PUT'])
# def update_client(client_id):
#     client = Clients.query.get(client_id)
#     # ver que se puede modificar


# @app.route('/delte_client/<int:client_id>', methods = ['DELETE'])
# def delete_client(client_id):
#     client = Clients.query.get(client_id)
#     db.session.delete(client)
#     db.session.commit()
#     return jsonify(message_succsess)