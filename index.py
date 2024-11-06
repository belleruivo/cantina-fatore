from flask import Flask, render_template, request, session, make_response
import pymysql

app = Flask(__name__)

app.secret_key = "9wefjfsdfsdaodaofjejcaqwqwewqeoooopwq"

# criar o banco de dados cantina_fatore em casa!
# db = pymysql.connect(host="localhost", user="root", password="", database="cantina_fatore")

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == "GET":
        
        if request.cookies.get("usuario"):
            resp = make_response("Site da cantina com cookie setado.")            
        else:
            resp = make_response("Site sem cookie")
            resp.set_cookie('usuario', 'isabelle')  
            
        # cursor = db.cursor()
        # sql = "SELECT * FROM clientes"
        # cursor.execute(sql)
        # results = cursor.fetchall()
        # print(results)
                  
        return resp
        
        # return render_template("index.html",content=['banana','pera','maca'])
        
    else:
        return "O que veio do meu form: "+request.form['conteudo']