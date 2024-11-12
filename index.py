from app import create_app
# da pasta app ele importou o create_app que tá no __init__.py

app = create_app() # instancia a aplicação

if __name__ == "__main__":
    # roda a aplicação no localhost na porta 5000, com o debug ativado porém não rolou precisa rodar o flask debug (modo desenvolvimento)
    app.run(debug=True)
