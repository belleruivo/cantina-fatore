import pymysql

def get_all_clients():
    # conexao com o banco
    db = pymysql.connect(host="localhost", user="root", password="", database="cantina_fatore")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM clientes")
    results = cursor.fetchall()

    # fecha conexao
    cursor.close()
    db.close()

    return results