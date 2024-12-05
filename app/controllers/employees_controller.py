from flask import render_template, request, redirect, url_for
from app.models.employees_model import obter_todos_funcionarios, adicionar_funcionario, atualizar_funcionario, excluir_funcionario as excluir_funcionario_model

def employees_list():
    # Recupera a lista de funcionários
    funcionarios = obter_todos_funcionarios()
    return render_template("employees.html", funcionarios=funcionarios, show_sidebar=True)

def salvar_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        adicionar_funcionario(nome)
        return redirect(url_for('funcionarios'))

def editar_funcionario(id):
    if request.method == 'POST':
        nome = request.form['nome']
        atualizar_funcionario(id, nome)
        return redirect(url_for('funcionarios'))

def excluir_funcionario(id):
    excluir_funcionario_model(id)  
    return redirect(url_for('funcionarios'))
