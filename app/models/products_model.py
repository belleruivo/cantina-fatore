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
