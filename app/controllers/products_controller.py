from flask import render_template, redirect, url_for, request, flash, jsonify
from app.models.products_model import Produto
from app.models.vendas_model import Venda
from app.models.employees_model import FuncionarioRepository
from app.controllers.interface_controller import CadastroInterface, AtualizacaoInterface, RemocaoInterface, ListagemInterface

import os

class CRUDProduto(CadastroInterface, AtualizacaoInterface, RemocaoInterface, ListagemInterface):
    def cadastrar(self):
        if request.method == 'POST':
            nome = request.form['nome']
            preco = request.form['preco']
            categoria = request.form['categoria']
            quantidade_estoque = request.form['quantidade']
            foto = request.files['foto'] if 'foto' in request.files else None

            # onde as fotos serão salvas
            upload_dir = os.path.join('app', 'static', 'uploads')

            # garante que o diretório existe
            os.makedirs(upload_dir, exist_ok=True)

            foto_caminho = None
            if foto:
                # nome seguro para evitar problemas
                from werkzeug.utils import secure_filename
                foto_nome = secure_filename(foto.filename)
                foto_caminho = os.path.join(upload_dir, foto_nome)

                foto.save(foto_caminho)

                # armazena apenas o caminho relativo a partir de 'static/uploads'
                foto_caminho = os.path.join('uploads', foto_nome)

            Produto.adicionar_produto(nome, preco, categoria, quantidade_estoque, foto_caminho)

            return redirect(url_for('product_list'))

    def atualizar(self, id):
        if request.method == 'POST':
            nome = request.form['nome']
            preco = request.form['preco']
            categoria = request.form['categoria']
            quantidade_estoque = request.form['quantidade']
            foto = request.files['foto'] if 'foto' in request.files else None

            foto_caminho = None
            if foto:
                from werkzeug.utils import secure_filename
                foto_nome = secure_filename(foto.filename)
                foto_caminho = os.path.join('app', 'static', 'uploads', foto_nome)
                foto.save(foto_caminho)

                # armazena apenas o caminho relativo a partir de 'static/uploads'
                foto_caminho = os.path.join('uploads', foto_nome)

            Produto.atualizar_produto(id, nome, preco, categoria, quantidade_estoque, foto_caminho)
            return redirect(url_for('product_list'))
        
    def remover(self, id):
        Produto.excluir_produto(id)
        return redirect(url_for('product_list'))

    def listar(self):
        query = request.args.get('query')
        if query:
            produtos = Produto.buscar_produtos(query)
        else:
            produtos = Produto.obter_todos_produtos()
        
        # recupera itens do carrinho e o total
        itens_carrinho, total = Venda.obter_itens_carrinho()

        funcionarios = FuncionarioRepository.obter_todos_funcionarios()  
        return render_template(
            "products.html",
            produtos=produtos,
            itens_carrinho=itens_carrinho,
            total=total,
            funcionarios=funcionarios,
            show_sidebar=True
        )
