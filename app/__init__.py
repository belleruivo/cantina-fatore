from flask import Flask
from app.controllers.main_controller import home
from app.controllers.products_controller import product_list
from app.controllers.login_controller import LoginController # ali dps de import vai o nome da classe ou método
from app.controllers.employees_controller import employees_list
from app.controllers.sales_controller import sales_list
from app.controllers.reports_controller import reports

# inicializa os pacotes
def create_app():
    app = Flask(__name__)
    app.secret_key = "9wefjfsdfsdaodaofjejcaqwqwewqeoooopwq"

    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/login', 'login', LoginController.login, methods=["GET", "POST"])  
    app.add_url_rule('/logout', 'logout', LoginController.logout)  
    app.add_url_rule('/produtos', 'product_list', product_list)
    app.add_url_rule('/funcionarios', 'funcionarios', employees_list)
    app.add_url_rule('/vendas_do_dia', 'vendas_do_dia', sales_list)
    app.add_url_rule('/relatorios', 'relatorios', reports)  
    # esses 3 "parâmetros" são: o caminho da rota, o nome da rota (usado em layout) e o nome da função ou método que será executado ao acessar aquela rota.
    
    return app
