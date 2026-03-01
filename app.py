from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/produits")
def produits():
    return "<p>produits</p>"

@app.route("/panier")
def panier():
    return "<p>panier</p>"

@app.route("/contacts")
def contacts():
    return "<p>contact</p>"
