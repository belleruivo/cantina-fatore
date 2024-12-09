# depois de import vai o nome da classe ou método
from flask import Flask
from app.controllers.main_controller import home
from app.controllers.products_controller import CRUDProduto
from app.controllers.vendas_controller import GerenciarVendas
from app.controllers.login_controller import LoginController, login_required 
from app.controllers.reports_controller import RelatorioVendas
from app.models.employees_model import FuncionarioRepository
from app.models.products_model import ProdutoRepository
from app.models.vendas_model import VendaRepository
from app.controllers.employees_controller import CRUDFuncionario


# inicializa os pacotes
def create_app():
    app = Flask(__name__)
    app.secret_key = "9wefjfsdfsdaodaofjejcaqwqwewqeoooopwq"

    funcionario_repository = FuncionarioRepository()
    produto_repository = ProdutoRepository()
    venda_repository = VendaRepository()

    funcionario = CRUDFuncionario(funcionario_repository)
    produto = CRUDProduto(produto_repository)
    venda = GerenciarVendas(venda_repository)
    relatorio = RelatorioVendas()

    # esses 3 "parâmetros" são: o caminho da rota, o nome da rota (usado em layout) e o nome da função ou método que será executado ao acessar aquela rota.
    app.add_url_rule('/', 'home', home) 
    app.add_url_rule('/login', 'login', LoginController.login, methods=["GET", "POST"]) 
    app.add_url_rule('/logout', 'logout', LoginController.logout) 
    app.add_url_rule('/produtos', 'product_list', login_required(produto.listar))  
    app.add_url_rule('/produtos/editar/<int:id>', 'editar_produto', login_required(produto.atualizar), methods=['GET', 'POST'])  
    app.add_url_rule('/produtos/excluir/<int:id>', 'excluir_produto', login_required(produto.remover), methods=["POST"])  
    app.add_url_rule('/produtos/vender/<int:id>', 'vender_produto', login_required(venda.vender_produto), methods=["POST"])  
    app.add_url_rule('/produtos/salvar', 'salvar_produto', login_required(produto.cadastrar), methods=['POST'])  
    app.add_url_rule('/funcionarios', 'funcionarios', login_required(funcionario.listar)) 
    app.add_url_rule('/funcionarios/adicionar', 'salvar_funcionario', login_required(funcionario.cadastrar), methods=['POST'])
    app.add_url_rule('/funcionarios/editar/<int:id>', 'editar_funcionario', login_required(funcionario.atualizar), methods=['POST'])
    app.add_url_rule('/funcionarios/excluir/<int:id>', 'excluir_funcionario', login_required(funcionario.remover), methods=['POST'])

    app.add_url_rule('/relatorios', 'relatorios', login_required(relatorio.gerar_relatorio_vendas))
    app.add_url_rule('/download/relatorio-geral', 'download_relatorio_geral', login_required(relatorio.download_relatorio))
    
    app.add_url_rule('/remover/<int:carrinho_id>', 'remover_produto_do_carrinho',  login_required(venda.remover_produto_do_carrinho), methods=['POST'])
    app.add_url_rule('/registrar-venda', 'registrar_venda', login_required(venda.registrar_venda), methods=['POST'])
    
    return app
