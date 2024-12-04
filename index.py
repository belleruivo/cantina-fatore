# da pasta app ele importou o create_app que tá no __init__.py
from app import create_app

# instancia a aplicação
app = create_app() 

if __name__ == "__main__":
    # roda a aplicação no localhost na porta 5000, com o debug ativado. por via da dúvidas rodar o flask debug (modo desenvolvimento)
    app.run(debug=True)
