from flask import render_template, request, redirect, url_for
from app.models.employees_model import Funcionario, FuncionarioRepository
#from app.repositories.funcionario_repository import FuncionarioRepository
from app.controllers.interface_controller import CadastroInterface, AtualizacaoInterface, RemocaoInterface, ListagemInterface

class CRUDFuncionario(CadastroInterface, AtualizacaoInterface, RemocaoInterface, ListagemInterface):
    def __init__(self, funcionario_repository: FuncionarioRepository):
        self.funcionario_repository = funcionario_repository # Injeção de dependência do repositório**

    def cadastrar(self):
        if request.method == 'POST':
            nome = request.form['nome']
            self.funcionario_repository.salvar(nome)  
            return redirect(url_for('funcionarios'))

    def atualizar(self, id):
        if request.method == 'POST':
            nome = request.form['nome']
            self.funcionario_repository.atualizar(id, nome) 
            return redirect(url_for('funcionarios'))

    def remover(self, id):
        self.funcionario_repository.excluir(id)  
        return redirect(url_for('funcionarios'))

    def listar(self):
        funcionarios_data = self.funcionario_repository.obter_todos_funcionarios()  
        funcionarios = [Funcionario(id=linha[0], nome=linha[1], total_gasto=linha[2]) for linha in funcionarios_data]
        return render_template("employees.html", funcionarios=funcionarios, show_sidebar=True)

