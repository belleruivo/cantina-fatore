class LoginModel:
    # (isabelle) -> previnir mysql injection!
    # credenciais predefinidas no código, user e senha
    USUARIOS = {
        "admin": "admin123"
    }

    @staticmethod
    def verificar_login(nome_usuario, senha):
        # verifica se o nome de usuário e a senha estão corretos
        if nome_usuario in LoginModel.USUARIOS and LoginModel.USUARIOS[nome_usuario] == senha:
            return True
        return False
