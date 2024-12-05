from flask import render_template, redirect, url_for, request, flash, jsonify
from app.models.products_model import obter_todos_produtos, buscar_produtos, obter_itens_carrinho, adicionar_ao_carrinho, remover_do_carrinho, atualizar_produto, adicionar_produto, salvar_venda_db
from app.models.employees_model import obter_todos_funcionarios
from app.utils.database import get_db_connection  

import os

def product_list():
    query = request.args.get('query')
    if query:
        produtos = buscar_produtos(query)
    else:
        produtos = obter_todos_produtos()
    
    # recupera itens do carrinho e o total
    itens_carrinho, total = obter_itens_carrinho()

    funcionarios = obter_todos_funcionarios()  # Adicione esta linha
    return render_template(
        "products.html",
        produtos=produtos,
        itens_carrinho=itens_carrinho,
        total=total,
        funcionarios=funcionarios,  # Adicione esta linha
        show_sidebar=True
    )

def salvar_produto():
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

        adicionar_produto(nome, preco, categoria, quantidade_estoque, foto_caminho)

        return redirect(url_for('product_list'))

def editar_produto(id):
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

        atualizar_produto(id, nome, preco, categoria, quantidade_estoque, foto_caminho)
        return redirect(url_for('product_list'))

def excluir_produto(id):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for('product_list'))

from flask import render_template, redirect, url_for, request, flash  # Adicione o flash aqui

def vender_produto(id):
    quantidade = int(request.form.get('quantidade', 1))
    sucesso, mensagem = adicionar_ao_carrinho(id, quantidade)
    
    if not sucesso:
        flash(mensagem, 'error')
    else:
        flash(mensagem, 'success')
        
    return redirect(url_for('product_list'))

def remover_produto_do_carrinho(carrinho_id):
    remover_do_carrinho(carrinho_id)
    return redirect(url_for('product_list'))

def registrar_venda():
    try:
        dados = request.json
        comprador_tipo = dados['comprador_tipo']
        comprador_id = dados['comprador_id'] if comprador_tipo == 'funcionario' else None  # Alterado de 0 para None
        valores_pagamento = {
            'dinheiro': float(dados['valor_dinheiro'] or 0),
            'cartao': float(dados['valor_cartao'] or 0),
            'pix': float(dados['valor_pix'] or 0)
        }
        
        # resto do código continua igual
        
        # Obter itens do carrinho
        itens_carrinho, total = obter_itens_carrinho()
        
        # Validar o total
        total_pagamento = sum(valores_pagamento.values())
        if total_pagamento != total:
            return jsonify({'success': False, 'message': 'Valores de pagamento não conferem com o total'}), 400
            
        sucesso, mensagem = salvar_venda_db(  # Alterado aqui
            comprador_tipo,
            comprador_id,
            valores_pagamento,
            itens_carrinho,
            total
        )
        
        if sucesso:
            flash(mensagem, 'success')
            return jsonify({'success': True, 'message': mensagem})
        else:
            flash(mensagem, 'error')
            return jsonify({'success': False, 'message': mensagem}), 400
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
