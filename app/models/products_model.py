# app/models/produto_model.py
class Produto:
    def __init__(self, id, nome, preco, categoria, quantidade_estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade_estoque = quantidade_estoque

    def __str__(self):
        return f"Produto({self.id}, {self.nome}, {self.preco}, {self.categoria}, {self.quantidade_estoque})"

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
