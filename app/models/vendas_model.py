from app.utils.database import get_db_connection
"""tiraria daqui e colocaria em uma pasta de banco, assim como está no diagrama"""

class Venda: 
    def adicionar_ao_carrinho(produto_id, quantidade):
        conexao = get_db_connection()
        cursor = conexao.cursor()

        # Verifica quantidade em estoque
        cursor.execute("SELECT quantidade_estoque FROM produtos WHERE id = %s", (produto_id,))
        estoque = cursor.fetchone()[0]

        # Verifica quantidade atual no carrinho
        cursor.execute("SELECT COALESCE(SUM(quantidade), 0) FROM carrinho WHERE produto_id = %s", (produto_id,))
        quantidade_no_carrinho = cursor.fetchone()[0]

        # Calcula quantidade total após adicionar
        quantidade_total = quantidade_no_carrinho + quantidade

        # Se a quantidade total ultrapassar o estoque, não permite a adição
        if quantidade_total > estoque:
            conexao.close()
            return False, f"Quantidade indisponível. Estoque: {estoque}, No carrinho: {quantidade_no_carrinho}"
        
        # Se o produto já está no carrinho, atualiza a quantidade
        if quantidade_no_carrinho > 0:
            cursor.execute("""
                UPDATE carrinho
                SET quantidade = %s
                WHERE produto_id = %s
            """, (quantidade_total, produto_id))
        else:
            # Caso contrário, adiciona o produto ao carrinho
            cursor.execute("""
                INSERT INTO carrinho (produto_id, quantidade)
                VALUES (%s, %s)
            """, (produto_id, quantidade))
        
        conexao.commit()
        conexao.close()
        return True, "Produto adicionado ao carrinho com sucesso!"


    def obter_itens_carrinho():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        
        # Modifique a query para pegar o ID do produto corretamente
        cursor.execute("""
            SELECT c.id as carrinho_id, p.id as produto_id, p.nome, c.quantidade, p.preco 
            FROM carrinho c 
            JOIN produtos p ON c.produto_id = p.id
        """)
        
        itens = cursor.fetchall()
        total = sum(item[3] * item[4] for item in itens)  # quantidade * preco
        
        conexao.close()
        return itens, total


    def remover_do_carrinho(carrinho_id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        
        # obtém a quantidade atual no carrinho
        cursor.execute("SELECT quantidade FROM carrinho WHERE id = %s", (carrinho_id,))
        resultado = cursor.fetchone()

        if resultado:
            quantidade_atual = resultado[0]
            if quantidade_atual > 1:
                # decrementa a quantidade
                nova_quantidade = quantidade_atual - 1
                cursor.execute("""
                    UPDATE carrinho
                    SET quantidade = %s
                    WHERE id = %s
                """, (nova_quantidade, carrinho_id))
            else:
                # remove o registro se a quantidade for 1
                cursor.execute("DELETE FROM carrinho WHERE id = %s", (carrinho_id,))
        
        conexao.commit()
        conexao.close()

    def salvar_venda_db(comprador_tipo, comprador_id, valores_pagamento, itens_carrinho, total):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        
        try:
            # Inserir a venda
            cursor.execute("""
                INSERT INTO vendas (
                    comprador_tipo, 
                    comprador_id,
                    total,
                    valor_dinheiro,
                    valor_cartao,
                    valor_pix
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                comprador_tipo,
                comprador_id,
                total,
                valores_pagamento.get('dinheiro', 0),
                valores_pagamento.get('cartao', 0),
                valores_pagamento.get('pix', 0)
            ))
            
            venda_id = cursor.lastrowid
            
            # Inserir os itens da venda
            for item in itens_carrinho:
                # item agora é uma tupla: (carrinho_id, produto_id, nome, quantidade, preco)
                cursor.execute("""
                    INSERT INTO itens_venda (
                        venda_id,
                        produto_id,
                        quantidade,
                        valor_unitario,
                        subtotal
                    ) VALUES (%s, %s, %s, %s, %s)
                """, (
                    venda_id,
                    item[1],  # produto_id (índice 1)
                    item[3],  # quantidade (índice 3)
                    item[4],  # valor_unitario (índice 4)
                    item[3] * item[4]  # subtotal = quantidade * valor_unitario
                ))
                
                # Atualizar o estoque
                cursor.execute("""
                    UPDATE produtos 
                    SET quantidade_estoque = quantidade_estoque - %s 
                    WHERE id = %s
                """, (item[3], item[1]))  # quantidade e produto_id
            
            # Limpar o carrinho
            cursor.execute("DELETE FROM carrinho")
            
            conexao.commit()
            return True, "Venda registrada com sucesso!"
            
        except Exception as e:
            conexao.rollback()
            return False, f"Erro ao registrar venda: {str(e)}"
            
        finally:
            conexao.close()