from app.utils.database import get_db_connection

''' PRINCÍPIO DA RESPONSABILIDADE ÚNICA: a classe FuncionarioRepository é responsável por salvar, excluir, atualizar e obter todos os funcionários.'''

class Funcionario:
    def __init__(self, id=None, nome=None, total_gasto=0.00):
        self.id = id
        self.nome = nome
        self.total_gasto = total_gasto

    def __str__(self):
        return f"Funcionario({self.id}, {self.nome}, {self.total_gasto})"
class FuncionarioRepository:
    @staticmethod
    def salvar(nome, total_gasto=0.00):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO funcionarios (nome, total_gasto) VALUES (%s, %s)
        """, (nome, total_gasto))
        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("UPDATE vendas SET comprador_id = NULL WHERE comprador_id = %s", (id,))
        conexao.commit()
        cursor.execute("DELETE FROM funcionarios WHERE id = %s", (id,))
        conexao.commit()
        conexao.close()

    @staticmethod
    def atualizar(id, nome):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE funcionarios SET nome = %s WHERE id = %s
        """, (nome, id))
        conexao.commit()
        conexao.close()

    @staticmethod
    def obter_todos_funcionarios():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, total_gasto FROM funcionarios")
        resultados = cursor.fetchall()
        conexao.close()

        funcionarios = [Funcionario(id=linha[0], nome=linha[1], total_gasto=linha[2]) for linha in resultados]
        
        # Bubble Sort 
        n = len(funcionarios)
        for i in range(n):
            for j in range(0, n - i - 1):
                if funcionarios[j].nome.lower() > funcionarios[j + 1].nome.lower():
                    funcionarios[j], funcionarios[j + 1] = funcionarios[j + 1], funcionarios[j]

        return funcionarios


