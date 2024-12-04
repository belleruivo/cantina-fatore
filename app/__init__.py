from flask import Flask
from app.controllers.main_controller import home
from app.controllers.products_controller import product_list
from app.controllers.login_controller import LoginController # ali dps de import vai o nome da classe ou método
from app.controllers.products_controller import editar_produto
from app.controllers.products_controller import excluir_produto
from app.controllers.products_controller import vender_produto
from app.controllers.employees_controller import employees_list
from app.controllers.sales_controller import sales_list
from app.controllers.reports_controller import reports
from app.controllers.products_controller import salvar_produto
from app.controllers.login_controller import login_required  
from app.controllers.products_controller import remover_produto_do_carrinho

# inicializa os pacotes
def create_app():
    app = Flask(__name__)
    app.secret_key = "9wefjfsdfsdaodaofjejcaqwqwewqeoooopwq"

    app.add_url_rule('/', 'home', home) 
    app.add_url_rule('/login', 'login', LoginController.login, methods=["GET", "POST"]) 
    app.add_url_rule('/logout', 'logout', LoginController.logout) 
    app.add_url_rule('/produtos', 'product_list', login_required(product_list))  
    app.add_url_rule('/produtos/editar/<int:id>', 'editar_produto', login_required(editar_produto), methods=['GET', 'POST'])  
    app.add_url_rule('/produtos/excluir/<int:id>', 'excluir_produto', login_required(excluir_produto), methods=["POST"])  
    app.add_url_rule('/produtos/vender/<int:id>', 'vender_produto', login_required(vender_produto), methods=["POST"])  
    app.add_url_rule('/funcionarios', 'funcionarios', login_required(employees_list))  
    app.add_url_rule('/vendas_do_dia', 'vendas_do_dia', login_required(sales_list))  
    app.add_url_rule('/relatorios', 'relatorios', login_required(reports))  
    app.add_url_rule('/produtos/salvar', 'salvar_produto', login_required(salvar_produto), methods=['POST'])  
    app.add_url_rule('/remover/<int:carrinho_id>', 'remover_produto_do_carrinho',  login_required(remover_produto_do_carrinho), methods=['POST'])
    # esses 3 "parâmetros" são: o caminho da rota, o nome da rota (usado em layout) e o nome da função ou método que será executado ao acessar aquela rota.
    
    return app
