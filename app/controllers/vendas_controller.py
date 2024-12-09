from flask import redirect, url_for, request, flash, jsonify
from app.models.vendas_model import Venda
from decimal import Decimal

class CRUDVendas:
    @staticmethod
    def vender_produto(id):
        quantidade = int(request.form.get('quantidade', 1))
        sucesso, mensagem = Venda.adicionar_ao_carrinho(id, quantidade)
        
        if not sucesso:
            flash(mensagem, 'error')
        else:
            flash(mensagem, 'success')
            
        return redirect(url_for('product_list'))

    @staticmethod
    def remover_produto_do_carrinho(carrinho_id):
        Venda.remover_do_carrinho(carrinho_id)
        return redirect(url_for('product_list'))

    @staticmethod
    def registrar_venda():
        try:
            dados = request.json
            comprador_tipo = dados['comprador_tipo']
            comprador_id = dados['comprador_id'] if comprador_tipo == 'funcionario' else None
            
            # Use Decimal para valores financeiros
            valores_pagamento = {
                'dinheiro': Decimal(dados['valor_dinheiro'] or '0.00'),
                'cartao': Decimal(dados['valor_cartao'] or '0.00'),
                'pix': Decimal(dados['valor_pix'] or '0.00')
            }
            
            # Obter itens do carrinho
            itens_carrinho, total = Venda.obter_itens_carrinho()
            total = Decimal(str(total))  # Certifique-se de que o total também seja um Decimal
            
            # Validar o total
            total_pagamento = sum(valores_pagamento.values())
            if total_pagamento != total:
                return jsonify({'success': False, 'message': 'Valores de pagamento não conferem com o total'}), 400

            # Salvar venda no banco de dados
            sucesso, mensagem = Venda.salvar_venda_db(
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