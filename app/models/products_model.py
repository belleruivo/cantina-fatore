from flask import flash, url_for, redirect

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

# funções relacionadas ao banco
from app.utils.database import get_db_connection

def buscar_produtos(query):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE nome LIKE %s", ('%' + query + '%',))
    resultados = cursor.fetchall()
    conexao.close()
    
    # converte para objetos Produto
    produtos = [Produto(*linha) for linha in resultados]
    return produtos

def obter_todos_produtos():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    resultados = cursor.fetchall()
    conexao.close()
    
    print(resultados)
    
    # converte para objetos Produto
    produtos = [Produto(*linha) for linha in resultados]
    return produtos

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

def adicionar_ao_carrinho(produto_id, quantidade):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute("SELECT quantidade_estoque FROM produtos WHERE id = %s", (produto_id,))
    estoque = cursor.fetchone()[0]

    if quantidade > estoque:
        quantidade = estoque  
    
    # verifica se o produto já está no carrinho
    cursor.execute("SELECT quantidade FROM carrinho WHERE produto_id = %s", (produto_id,))
    produto_existente = cursor.fetchone()

    if produto_existente:
        # se o produto já existe no carrinho, atualiza a quantidade
        nova_quantidade = produto_existente[0] + quantidade
        cursor.execute("""
            UPDATE carrinho
            SET quantidade = %s
            WHERE produto_id = %s
        """, (nova_quantidade, produto_id))
    else:
        # caso contrário, adiciona o produto ao carrinho
        cursor.execute("""
            INSERT INTO carrinho (produto_id, quantidade)
            VALUES (%s, %s)
        """, (produto_id, quantidade))
    
    conexao.commit()
    conexao.close()


def obter_itens_carrinho():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    
    # query para obter os itens e calcular o subtotal por produto
    cursor.execute("""
        SELECT c.id, p.nome, SUM(c.quantidade) as quantidade, p.preco, 
               SUM(c.quantidade * p.preco) as subtotal
        FROM carrinho c
        JOIN produtos p ON c.produto_id = p.id
        GROUP BY c.produto_id, c.id
    """)
    itens = cursor.fetchall()

    # calcula o total somando os subtotais
    total = sum(item[4] for item in itens)

    conexao.close()
    return itens, total


def remover_do_carrinho(carrinho_id):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    
    # obtém a quantidade atual no carrinho
    cursor.execute("SELECT quantidade FROM carrinho WHERE id = %s", (carrinho_id,))
    resultado = cursor.fetchone()

    if resultado:
        quantidade_atual = resultado[0]
        if quantidade_atual > 1:
            # decrementa a quantidade
            nova_quantidade = quantidade_atual - 1
            cursor.execute("""
                UPDATE carrinho
                SET quantidade = %s
                WHERE id = %s
            """, (nova_quantidade, carrinho_id))
        else:
            # remove o registro se a quantidade for 1
            cursor.execute("DELETE FROM carrinho WHERE id = %s", (carrinho_id,))
    
    conexao.commit()
    conexao.close()

