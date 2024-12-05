from app.utils.database import get_db_connection

class Funcionario:
    def __init__(self, id, nome, total_gasto=0.00):
        self.id = id
        self.nome = nome
        self.total_gasto = total_gasto

    def __str__(self):
        return f"Funcionario({self.id}, {self.nome}, {self.total_gasto})"

# Funções relacionadas ao banco de dados
def obter_todos_funcionarios():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    resultados = cursor.fetchall()
    print(resultados)  # Adicione essa linha para verificar os resultados
    conexao.close()

    # Converte para objetos Funcionario
    funcionarios = [Funcionario(*linha) for linha in resultados]
    return funcionarios


def adicionar_funcionario(nome):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO funcionarios (nome, total_gasto) VALUES (%s, %s)
    """, (nome, 0.00))
    conexao.commit()
    conexao.close()

def atualizar_funcionario(id, nome):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE funcionarios SET nome = %s WHERE id = %s
    """, (nome, id))
    conexao.commit()
    conexao.close()

def excluir_funcionario(id):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM funcionarios WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()
