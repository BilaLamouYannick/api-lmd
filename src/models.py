from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from datetime import datetime
from sqlalchemy_utils import EmailType, PasswordType, force_auto_coercion
from . import db

force_auto_coercion()

class Commande(db.Model):
    __tablename__ = 'Commande'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)


class Panier(db.Model):
    __tablename__ = 'Panier'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    number_produit = db.Column(db.Integer)
    total = db.Column(db.Integer)

class Users(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    prenom = db.Column(db.String(80), unique=False, nullable=False)
    sexe = db.Column(db.CHAR(), unique=False, nullable=False)
    phone = db.Column(db.Integer)
    email = db.Column(EmailType)
    password = db.Column(
        PasswordType(schemes=['pbkdf2_sha512']), 
        unique=False,  
        nullable=False, 
    )

    def __repr__ (self):
        return '<User {}>'.format(self.name)

class Employes(Users):
    __tablename__ = 'Emplotes'
    is_employe = db.Column(db.Boolean, unique=False, default=False)


class Clients(Users):
    __tablename__ = 'Clients'
    panier_id = db.Column(db.Integer, db.ForeignKey('Panier.id'), nullable=False)
    is_client = db.Column(db.Boolean, unique=False, default=False)

class Admin(Users):
    __tablename__ = 'Admin'
    is_admin = db.Column(db.Boolean, unique=False, default=False)

class Annonceur(db.Model):
    __tablename__ = 'Annonceur'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    entreprise = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.Integer)
    email = db.Column(EmailType)

    def __repr__ (self):
        return '<Annonceur {}>'.format(self.entreprise)

class Annonce(db.Model):
    __tablename__ = 'Annonce'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    annonceur_id = db.Column(db.Integer, db.ForeignKey('Annonceur.id'), nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_actif = db.Column(db.Boolean, unique=False, default=False)
    image = db.Column(db.String(80), nullable=False)

    def __repr__ (self):
        return '<Annonce {}>'.format(self.name)


class Categorie(db.Model):
    __tablename__ = 'Categorie'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__ (self):
        return '<Categorie {}>'.format(self.name)    

class Marque(db.Model):
    __tablename__ = 'Marque'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)    
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__ (self):
        return '<Marque {}>'.format(self.name)

class Produits(db.Model):
    __tablename__ = 'Produit'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    categorie_id = db.Column(db.Integer, db.ForeignKey('Categorie.id'), nullable=False)
    marque_id = db.Column(db.Integer, db.ForeignKey('Marque.id'), nullable=False)
    designation = db.Column(db.String(80), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)

    def __repr__ (self):
        return '<Produit {}>'.format(self.designation)
