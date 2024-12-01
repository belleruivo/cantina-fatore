from flask import render_template, redirect, url_for, request
from app.models.products_model import obter_todos_produtos
from app.models.products_model import atualizar_produto
from app.utils.database import get_db_connection  
from app.models.products_model import adicionar_produto

import os

def product_list():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    
    produtos = obter_todos_produtos()  # usa a função que já converte os dados em objetos Produto
    return render_template("products.html", produtos=produtos, show_sidebar=True)


def salvar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        categoria = request.form['categoria']
        quantidade_estoque = request.form['quantidade']
        foto = request.files['foto'] if 'foto' in request.files else None

        # onde as fotos serão salvas
        upload_dir = os.path.join('app', 'static', 'uploads')

        # garante que o diretório existe
        os.makedirs(upload_dir, exist_ok=True)

        foto_caminho = None
        if foto:
            # nome seguro para evitar problemas
            from werkzeug.utils import secure_filename
            foto_nome = secure_filename(foto.filename)
            foto_caminho = os.path.join(upload_dir, foto_nome)

            foto.save(foto_caminho)

            # armazena apenas o caminho relativo a partir de 'static/uploads'
            foto_caminho = os.path.join('uploads', foto_nome)

        adicionar_produto(nome, preco, categoria, quantidade_estoque, foto_caminho)

        return redirect(url_for('product_list'))

def editar_produto(id):
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        categoria = request.form['categoria']
        quantidade_estoque = request.form['quantidade']
        foto = request.files['foto'] if 'foto' in request.files else None

        foto_caminho = None
        if foto:
            from werkzeug.utils import secure_filename
            foto_nome = secure_filename(foto.filename)
            foto_caminho = os.path.join('app', 'static', 'uploads', foto_nome)
            foto.save(foto_caminho)

            # armazena apenas o caminho relativo a partir de 'static/uploads'
            foto_caminho = os.path.join('uploads', foto_nome)

        atualizar_produto(id, nome, preco, categoria, quantidade_estoque, foto_caminho)
        return redirect(url_for('product_list'))

def excluir_produto(id):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for('product_list'))

def vender_produto(id):
    quantidade = request.form.get('quantidade', 1)  # exemplo básico para capturar quantidade
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO carrinho (produto_id, quantidade) VALUES (%s, %s)", (id, quantidade))
    conexao.commit()
    conexao.close()
    return redirect(url_for('product_list'))