from flask import current_app as app
from flask import jsonify, request, make_response
from src.models import *
from src.modelSchema import *

prefix = app.config['API_ROOT'] + '/lmd_client'

# voire tous les produits du catalogue
@app.route(prefix + '/', methods=["GET"])
def index():
    # produits = Produits.query.all()
    # res = ProduitSchema.dump(produits)
    return jsonify({'page':'index'})

# voir toutes les categories
@app.route(prefix + '/allcategorie', methods=["GET"])
def getCategorie():
    all_categorie = Categorie.query.all()
    res = categories_schema.dump(all_categorie)
    return jsonify(res)