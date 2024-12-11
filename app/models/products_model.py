from flask import flash, url_for, redirect
from app.utils.database import get_db_connection

class Produto:
    def __init__(self, id, nome, preco, categoria, quantidade_estoque, foto):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade_estoque = quantidade_estoque
        self.foto = foto

    def __str__(self):
        return f"Produto({self.id}, {self.nome}, {self.preco}, {self.categoria}, {self.quantidade_estoque}, {self.foto})"

    '''METÓDOS DE CLASSE: Aqui estão os métodos de classe que interagem com o banco de dados.'''
class ProdutoRepository:
    @staticmethod
    def buscar_produtos(query, categoria=None):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        
        if categoria:
            cursor.execute("SELECT * FROM produtos WHERE nome LIKE %s AND categoria = %s", ('%' + query + '%', categoria))
        else:
            cursor.execute("SELECT * FROM produtos WHERE nome LIKE %s", ('%' + query + '%',))
        
        resultados = cursor.fetchall()
        conexao.close()
        
        # converte para objetos Produto
        produtos = [Produto(*linha) for linha in resultados]
        return produtos

    @staticmethod
    def obter_todos_produtos(categoria=None):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        
        if categoria:
            cursor.execute("SELECT * FROM produtos WHERE categoria = %s", (categoria,))
        else:
            cursor.execute("SELECT * FROM produtos")
        
        resultados = cursor.fetchall()
        conexao.close()
        
        # converte para objetos Produto
        produtos = [Produto(*linha) for linha in resultados]
        return produtos

    @staticmethod
    def adicionar_produto(nome, preco, categoria, quantidade_estoque, foto=None):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        
        # adiciona o produto no banco de dados
        cursor.execute("""
            INSERT INTO produtos (nome, preco, categoria, quantidade_estoque, foto)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, preco, categoria, quantidade_estoque, foto))
        
        conexao.commit()
        conexao.close()

    @staticmethod
    def atualizar_produto(id, nome, preco, categoria, quantidade_estoque, foto):
        conexao = get_db_connection()
        cursor = conexao.cursor()

        if foto:
            query = """
                UPDATE produtos
                SET nome = %s, preco = %s, categoria = %s, quantidade_estoque = %s, foto = %s
                WHERE id = %s
            """
            valores = (nome, preco, categoria, quantidade_estoque, foto, id)
        else:
            query = """
                UPDATE produtos
                SET nome = %s, preco = %s, categoria = %s, quantidade_estoque = %s
                WHERE id = %s
            """
            valores = (nome, preco, categoria, quantidade_estoque, id)

        cursor.execute(query, valores)
        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_produto(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
        conexao.commit()
        conexao.close()
        return redirect(url_for('product_list'))

