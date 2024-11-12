from flask import render_template, make_response, request
import pymysql

# conecta no banco de dados
def get_db_connection():
    return pymysql.connect(host="localhost", user="root", password="", database="cantina_fatore")

def home():
    db = get_db_connection()
    cursor = db.cursor()

    if request.method == "GET":
        if request.cookies.get("usuario"):
            resp = make_response("Site da cantina com cookie setado.")            
        else:
            resp = make_response("Site sem cookie")
            resp.set_cookie('usuario', 'isabelle')  
        
        cursor.execute("SELECT * FROM clientes")
        results = cursor.fetchall()
        print(results)  
        
        cursor.close()
        db.close()
        
        # aqui renderiza os resultados para templates
        return render_template("index.html", content=results)
        
    else:
        return "O que veio do meu form: " + request.form['conteudo']
