from flask import redirect, url_for, request, flash, jsonify
from app.models.vendas_model import VendaRepository
from decimal import Decimal

class GerenciarVendas:
    def __init__(self, venda_repository: VendaRepository):
        self.venda_repository = venda_repository # Injeção de dependência do repositório

    def vender_produto(self, id):
        quantidade = int(request.form.get('quantidade', 1))
        sucesso, mensagem = self.venda_repository.adicionar_ao_carrinho(id, quantidade)
        
        if not sucesso:
            flash(mensagem, 'error')
        else:
            flash(mensagem, 'success')
            
        return redirect(url_for('product_list'))

    def remover_produto_do_carrinho(self, carrinho_id):
        self.venda_repository.remover_do_carrinho(carrinho_id)
        return redirect(url_for('product_list'))

    def registrar_venda(self):
        try:
            dados = request.json
            comprador_tipo = dados['comprador_tipo']
            comprador_id = dados['comprador_id'] if comprador_tipo == 'funcionario' else None
            
            valores_pagamento = {
                'dinheiro': Decimal(dados['valor_dinheiro'] or '0.00'),
                'cartao': Decimal(dados['valor_cartao'] or '0.00'),
                'pix': Decimal(dados['valor_pix'] or '0.00')
            }
            
            itens_carrinho, total = self.venda_repository.obter_itens_carrinho()
            total = Decimal(str(total))  
            
            total_pagamento = sum(valores_pagamento.values())
            if total_pagamento != total:
                return jsonify({'success': False, 'message': 'Valores de pagamento não conferem com o total'}), 400
                
            sucesso, mensagem = self.venda_repository.salvar_venda_db(  # alterado aqui
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