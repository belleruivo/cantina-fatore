from app.utils.database import get_db_connection
from app.models.interface_controller import CRUDInterface

class Funcionario(CRUDInterface):
    def __init__(self, id=None, nome=None, total_gasto=0.00):
        self.id = id
        self.nome = nome
        self.total_gasto = total_gasto

    def __str__(self):
        return f"Funcionario({self.id}, {self.nome}, {self.total_gasto})"

    def salvar(self, nome):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO funcionarios (nome, total_gasto) VALUES (%s, %s)
        """, (nome, self.total_gasto))
        conexao.commit()
        conexao.close()

    def excluir(self, id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE id = %s", (id,))
        conexao.commit()
        conexao.close()

    def atualizar(self, id, nome):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE funcionarios SET nome = %s WHERE id = %s
        """, (nome, id))
        conexao.commit()
        conexao.close()


# Funções relacionadas ao banco de dados
def obter_todos_funcionarios():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    resultados = cursor.fetchall()
    conexao.close()

    # Converte para objetos Funcionario
    funcionarios = [Funcionario(id=linha[0], nome=linha[1], total_gasto=linha[2]) for linha in resultados]
    return funcionarios
