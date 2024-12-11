from flask import render_template, request, redirect, url_for
from app.models.employees_model import FuncionarioRepository
from app.controllers.interface_controller import CRUDInterface

''' PRINCÍPIO DE LISKOV: nesse caso, ele é cumprido, pois a classe CRUDFuncionario implementa as interfaces CadastroInterface, AtualizacaoInterface, RemocaoInterface e ListagemInterface. 
Em resumo, a classe CRUDFuncionario pode ser substituída por qualquer outra classe que implemente as mesmas interfaces.'''

'''PRINCÍPIO DA INJEÇÃO DE DEPENDÊNCIA: no construtor, a classe recebe uma instância de FuncionarioRepository, ou seja, a classe FuncionarioRepository é injetada na classe CRUDFuncionario.'''

'''POLIMORFISMO: usa um mesmo conjunto de métodos definido pela interface, mas com comportamentos específicos dependendo de cada classe.'''
class CRUDFuncionario(CRUDInterface):
    def __init__(self, funcionario_repository: FuncionarioRepository):
        self.funcionario_repository = funcionario_repository 

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
        funcionarios = self.funcionario_repository.obter_todos_funcionarios()  
        return render_template("employees.html", funcionarios=funcionarios, show_sidebar=True)

