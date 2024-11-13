from flask import Flask
from app.controllers.main_controller import home

# inicializa os pacotes

def create_app():
    app = Flask(__name__)
    app.secret_key = "9wefjfsdfsdaodaofjejcaqwqwewqeoooopwq"

    # aqui serão adicionadas as rotas como login etc.
    app.add_url_rule('/', 'home', home)

    return app
