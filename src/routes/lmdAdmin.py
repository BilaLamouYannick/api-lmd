from flask import current_app as app
from flask import jsonify, request, make_response
from src.models import *
from src.modelSchema import *

prefix = app.config['API_ROOT'] + '/lmd_admin'

# page d'index, voire le dashboard
@app.route(prefix + '/', methods=["GET"])
def index():
    return jsonify({'page':'index'})

# Lister tous les utilisateurs
@app.route(prefix + '/allusers', methods=["GET"])
def getUsers():
    all_users = Users.query.all()
    res = users_schema.dump(all_users)
    return jsonify(res)

# Afficher un utilisateur
@app.route(prefix + '/getuser/<id>', methods=["GET"])
def getUser(id):
    user = Users.query.get(id)
    res = user_schema.dump(user)
    return jsonify(res)

# Update un utlisateur
@app.route(prefix + '/updateuser/<id>', methods=["PUT"])
def updateUser(id):
    if request.method == "PUT":
        content = request.get_json()
        update_user = Users(
            name = content['name'],
            email = content['email'],
            password = content['password'],
        )
        #user = Users.query.get(id)

# Ajouter un utilisateur
@app.route(prefix + '/adduser', methods=["POST"])
def addUser():
    if request.method == "POST":
        content = request.get_json()
        new_User = Users(
            name=content['name'],
            prenom=content['prenom'],
            sexe=content['sexe'],
            phone=content['phone'],
            email=content['email'],
            password=content['password'],
            is_admin=content['is_admin']
        )
        db.session.add(new_User)
        db.session.commit()
        return make_response(f"L'utilisateur {new_User.name} a ete creer avec succes!")

# Ajouter une categorie
@app.route(prefix + '/addcategorie', methods=["POST"])
def addCategorie():
    if request.method == "POST":
        content = request.get_json()
        new_categorie = Categorie(
            name = content['name']
        )
        db.session.add(new_categorie)
        db.session.commit()
        return make_response(f"La categorie {new_categorie.name} a ete creer avec succes!")

# voir toutes les categories
@app.route(prefix + '/allcategorie', methods=["GET"])
def getCategorie():
    all_categorie = Categorie.query.all()
    res = categories_schema.dump(all_categorie)
    return jsonify(res)

# Ajouter une Marque
@app.route(prefix + '/addmarque', methods=["POST"])
def addMarque():
    if request.method == "POST":
        content = request.get_json()
        new_marque = Marque(
            name = content['name']
        )
        db.session.add(new_marque)
        db.session.commit()
        return make_response(f"La marque {new_marque.name} a ete creer avec succes!")

# voir la liste des marques
@app.route(prefix + '/allmarque', methods=["GET"])
def getMarque():
    all_marque = Categorie.query.all()
    res = marques_schema.dump(all_marque)
    return jsonify(res)

# Ajouter un produit
@app.route(prefix + '/addproduit', methods=["POST"])
def addProduit():
    if request.method == "POST":
        content = request.get_json()
        new_produit = Produits(
            categorie_id=content['categorie_id'],
            marque_id=content['marque_id'],
            designation=content['designation'],
            prix=content['prix'],
            number=content['number'],
            img=content['img'],
            description=content['description']
        )
        db.session.add(new_produit)
        db.session.commit()
        return make_response(f"Le produit {new_produit.designation} a ete creer avec succes!")

# lister tous les produits
@app.route(prefix + '/allproduits', methods=["GET"])
def getProduits():
    all_produits = Produits.query.all()
    res = produits_schema.dump(all_produits)
    return jsonify(res)