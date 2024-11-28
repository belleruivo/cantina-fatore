from flask import render_template, redirect, url_for, request
from app.models.products_model import obter_todos_produtos
from app.utils.database import get_db_connection  # Certifique-se de que o caminho esteja correto

def product_list():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    
    produtos = obter_todos_produtos()  # usa a função que já converte os dados em objetos Produto
    return render_template("products.html", produtos=produtos, show_sidebar=True)

def editar_produto(id):
    # aqui você buscaria o produto pelo ID e mostraria um formulário de edição
    return f"Editar produto {id}"

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