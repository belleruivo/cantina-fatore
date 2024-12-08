# depois de import vai o nome da classe ou método
from flask import Flask
from app.controllers.main_controller import home
from app.controllers.products_controller import product_list, editar_produto, excluir_produto, vender_produto, salvar_produto, remover_produto_do_carrinho, registrar_venda
from app.controllers.login_controller import LoginController, login_required 
from app.controllers.employees_controller import employees_list, salvar_funcionario, editar_funcionario, excluir_funcionario
from app.controllers.reports_controller import RelatorioVendas

# inicializa os pacotes
def create_app():
    app = Flask(__name__)
    app.secret_key = "9wefjfsdfsdaodaofjejcaqwqwewqeoooopwq"

    # esses 3 "parâmetros" são: o caminho da rota, o nome da rota (usado em layout) e o nome da função ou método que será executado ao acessar aquela rota.
    app.add_url_rule('/', 'home', home) 
    app.add_url_rule('/login', 'login', LoginController.login, methods=["GET", "POST"]) 
    app.add_url_rule('/logout', 'logout', LoginController.logout) 
    app.add_url_rule('/produtos', 'product_list', login_required(product_list))  
    app.add_url_rule('/produtos/editar/<int:id>', 'editar_produto', login_required(editar_produto), methods=['GET', 'POST'])  
    app.add_url_rule('/produtos/excluir/<int:id>', 'excluir_produto', login_required(excluir_produto), methods=["POST"])  
    app.add_url_rule('/produtos/vender/<int:id>', 'vender_produto', login_required(vender_produto), methods=["POST"])  
    app.add_url_rule('/produtos/salvar', 'salvar_produto', login_required(salvar_produto), methods=['POST'])  
    app.add_url_rule('/funcionarios', 'funcionarios', login_required(employees_list)) 
    app.add_url_rule('/funcionarios/adicionar', 'salvar_funcionario', salvar_funcionario, methods=['POST'])
    app.add_url_rule('/funcionarios/editar/<int:id>', 'editar_funcionario', editar_funcionario, methods=['POST'])
    app.add_url_rule('/funcionarios/excluir/<int:id>', 'excluir_funcionario', excluir_funcionario, methods=['POST'])

    app.add_url_rule('/relatorios', 'relatorios', login_required(RelatorioVendas.gerar_relatorio_vendas))
    app.add_url_rule('/download/relatorio-geral', 'download_relatorio_geral', login_required(RelatorioVendas.download_relatorio))
    
    app.add_url_rule('/remover/<int:carrinho_id>', 'remover_produto_do_carrinho',  login_required(remover_produto_do_carrinho), methods=['POST'])
    app.add_url_rule('/registrar-venda', 'registrar_venda', login_required(registrar_venda), methods=['POST'])
    
    return app
