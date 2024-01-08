from flask import Flask

app = Flask(__name__)#Iniciamos app

app.secret_key = "Llave secretaa"   #Se necesita para la sesión, es la manera en que se encripta