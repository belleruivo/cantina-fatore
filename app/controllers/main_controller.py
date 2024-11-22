from flask import render_template, make_response, request
from app.utils.database import get_db_connection # importa a funcao de conexao com banco

def home():
    # alguns testes no console
    if request.method == "GET":
        if request.cookies.get("usuario"):
            resp = make_response("Site da cantina com cookie setado.")            
        else:
            resp = make_response("Site sem cookie")
            resp.set_cookie('usuario', 'isabelle')  
        
        results = get_db_connection()
        
        # aqui renderiza os resultados para templates (login é a primeira página que abre)
        return render_template("login.html", content=results)
        
    else:
        return "O que veio do meu form: " + request.form['conteudo']
