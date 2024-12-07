from flask import render_template, request, redirect, url_for
from app.models.employees_model import Funcionario, obter_todos_funcionarios

funcionario_crud = Funcionario()

def employees_list():
    # Recupera a lista de funcionários
    funcionarios = obter_todos_funcionarios()
    return render_template("employees.html", funcionarios=funcionarios, show_sidebar=True)

def salvar_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        funcionario = Funcionario()  # Cria a instância do objeto Funcionario
        funcionario.salvar(nome)  # Usa a implementação CRUD para salvar
        return redirect(url_for('funcionarios'))

def editar_funcionario(id):
    if request.method == 'POST':
        nome = request.form['nome']
        funcionario = Funcionario(id=id)  # Cria a instância do objeto Funcionario
        funcionario.atualizar(id, nome)  # Usa a implementação CRUD para atualizar
        return redirect(url_for('funcionarios'))

def excluir_funcionario(id):
    funcionario = Funcionario(id=id)  # Cria a instância do objeto Funcionario
    funcionario.excluir(id)  # Usa a implementação CRUD para excluir
    return redirect(url_for('funcionarios'))
