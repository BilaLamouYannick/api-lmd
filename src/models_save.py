from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy_utils import EmailType, PasswordType, force_auto_coercion
from . import db

force_auto_coercion()

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
    is_admin = db.Column(db.Boolean, unique=False, default=False)

    def __init__(self, name, prenom, sexe, phone, email, password, is_admin):
        self.name = name
        self.prenom = prenom
        self.sexe = sexe
        self.phone = phone
        self.email = email
        self.password = password
        self.is_admin = is_admin

class Categorie(db.Model):
    __tablename__ = 'Categorie'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name    

class Marque(db.Model):
    __tablename__ = 'Marque'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)    
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

class Produits(db.Model):
    __tablename__ = 'Produit'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    categorie_id = db.Column(db.Integer, db.ForeignKey('Categorie.id'), nullable=False)
    marque_id = db.Column(db.Integer, db.ForeignKey('Marque.id'), nullable=False)
    designation = db.Column(db.String(80), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)

    def __init__(self, categorie_id, marque_id, designation, prix, number, img, description):
        self.categorie_id = categorie_id
        self.marque_id = marque_id
        self.designation = designation
        self.prix = prix
        self.number = number
        self.img = img
        self.description = description

class 