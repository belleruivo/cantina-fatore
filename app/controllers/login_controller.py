from flask import render_template, request, jsonify, session, redirect, url_for
from functools import wraps
from app.models.login_model import LoginModel

class LoginController:
    @staticmethod
    def login():
        if request.method == 'POST': 
            nome_usuario = request.form.get('nome_usuario').strip()
            senha = request.form.get('senha').strip()

            try:
                if LoginModel.verificar_login(nome_usuario, senha):
                    # salva o usuário na sessão
                    session['usuario'] = nome_usuario
                    return jsonify(success=True, redirect_url=url_for('product_list'))  # redireciona para /produtos
                else:
                    return jsonify(success=False, message="Credenciais inválidas. Tente novamente.")
            except Exception as e:
                return jsonify(success=False, message="Ocorreu um erro no servidor: " + str(e))
        
        # para o método GET, retorna o formulário de login
        return render_template('login.html', show_sidebar=False)

    @staticmethod
    def logout():
        session.pop('usuario', None)  # remove o usuário da sessão
        return redirect(url_for('login')) 

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            # redireciona para a página de login se o usuário não estiver logado
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function