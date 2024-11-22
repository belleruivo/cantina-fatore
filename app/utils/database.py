import pymysql

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="cantina_fatore",
        # port=3307 
        # na faculdade, descomentar a linha de port.
    )