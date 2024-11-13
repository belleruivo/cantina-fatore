from flask import render_template, make_response, request
from app.models.client_model import get_all_clients # importa a funcao de models

def home():
    if request.method == "GET":
        if request.cookies.get("usuario"):
            resp = make_response("Site da cantina com cookie setado.")            
        else:
            resp = make_response("Site sem cookie")
            resp.set_cookie('usuario', 'isabelle')  
        
        results = get_all_clients()
        
        # aqui renderiza os resultados para templates
        return render_template("index.html", content=results)
        
    else:
        return "O que veio do meu form: " + request.form['conteudo']
