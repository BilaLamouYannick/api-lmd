from . import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'prenom', 'sexe', 'phone')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class CategorieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

categorie_schema = CategorieSchema()
categories_schema = CategorieSchema(many=True)


class MarqueSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

marque_schema = MarqueSchema()
marques_schema = MarqueSchema(many=True)


class ProduitSchema(ma.Schema):
    class Meta:
        fields = ('id', 'categorie_id', 'marque_id', 'designation', 'prix', 'number', 'img', 'description')

produit_schema = ProduitSchema()
produits_schema = ProduitSchema(many=True)