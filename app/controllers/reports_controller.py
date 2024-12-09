import os
from flask import render_template, send_file
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from app.utils.database import get_db_connection

''' PRINCÍPIO DA RESPONSABILIDADE ÚNICA: 
Aplicado: Cada classe tem uma responsabilidade única. A classe BaseRelatorio é responsável apenas por salvar e formatar relatórios em Excel, enquanto a classe RelatorioVendas cuida de buscar dados de vendas e gerar o relatório específico.
Justificativa: A classe BaseRelatorio não lida com a lógica de negócios das vendas, apenas com a persistência e formatação de dados. A classe RelatorioVendas foca na obtenção e manipulação dos dados de vendas.'''

'''PRINCÍPIO DE ABERTURA/FECHAMENTO:
Aplicado: O código é projetado para ser aberto para extensão, mas fechado para modificação. Você pode adicionar novos tipos de relatórios (como RelatorioFuncionarios) sem modificar as classes existentes.
Justificativa: Ao adicionar uma nova classe como RelatorioFuncionarios, a estrutura de relatórios pode ser expandida sem modificar a classe BaseRelatorio ou RelatorioVendas.
'''

'''PRINCÍPIO DA SUBSTITUIÇÃO DE LISKOV:
Aplicado: A classe RelatorioVendas é uma subclasse de BaseRelatorio, e o comportamento da classe base pode ser substituído pela classe derivada sem alterar a integridade do programa.
Justificativa: RelatorioVendas pode ser usada no lugar de BaseRelatorio sem alterar a lógica, porque ambas as classes implementam métodos similares de manipulação de dados e arquivos Excel.
'''

'''STATIC METHOD:
Aplicado: Métodos como save_to_excel, format_excel, fetch_sales_data e gerar_relatorio_vendas são estáticos, pois não dependem do estado da instância da classe. Isso é ideal quando o comportamento não altera o estado de uma instância, mas precisa operar sobre dados fornecidos como argumentos.
'''

class BaseRelatorio:
    @staticmethod
    def save_to_excel(df, file_name, sheet_name):
        # caminho absoluto para o diretório de download no projeto
        download_dir = os.path.abspath(os.path.join(os.getcwd(), 'download_relatorio'))

        if not os.path.exists(download_dir):
            raise Exception(f"Diretório de download não existe: {download_dir}")
        
        file_path = os.path.join(download_dir, file_name)
        
        # exclui o arquivo anterior
        if os.path.exists(file_path):
            os.remove(file_path)

        # salva o arquivo Excel
        df.to_excel(file_path, index=False, sheet_name=sheet_name)

        # verifica se o arquivo foi criado corretamente
        if not os.path.exists(file_path):
            raise Exception(f"Erro ao salvar o arquivo: {file_path}")
        
        return file_path

    @staticmethod
    def format_excel(file_path):
        workbook = load_workbook(file_path)
        worksheet = workbook.active

        header_fill = PatternFill(start_color="4CAF50", end_color="4CAF50", fill_type="solid")
        header_font = Font(bold=True, color="FFFFFF")

        for cell in worksheet[1]:
            cell.font = header_font
            cell.fill = header_fill

        border = Border(
            left=Side(border_style="thin", color="000000"),
            right=Side(border_style="thin", color="000000"),
            top=Side(border_style="thin", color="000000"),
            bottom=Side(border_style="thin", color="000000"),
        )
        for row in worksheet.iter_rows():
            for cell in row:
                cell.border = border
                cell.alignment = Alignment(horizontal="center", vertical="center")

        # ajuste da largura das colunas
        for col in worksheet.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    max_length = max(max_length, len(str(cell.value) or ""))
                except:
                    pass
            worksheet.column_dimensions[column].width = max_length + 2

        workbook.save(file_path)

class RelatorioVendas(BaseRelatorio):
    @staticmethod
    def fetch_sales_data():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT v.id, v.comprador_tipo, f.nome AS comprador_nome, v.metodo_pagamento, v.total, v.data_venda
                          FROM vendas v
                          LEFT JOIN funcionarios f ON v.comprador_id = f.id''')
        vendas = cursor.fetchall()
        conn.close()
        return vendas

    @staticmethod
    def gerar_relatorio_vendas():
        vendas = RelatorioVendas.fetch_sales_data()
        df = pd.DataFrame(vendas, columns=["ID", "Comprador Tipo", "Comprador Nome", "Método Pagamento", "Total", "Data Venda"])
        file_path = RelatorioVendas.save_to_excel(df, 'relatorio_vendas.xlsx', 'Vendas')
        RelatorioVendas.format_excel(file_path)
        return render_template("reports.html", show_sidebar=True)

    @staticmethod
    def download_relatorio():
        file_path = os.path.join(os.getcwd(), 'download_relatorio', 'relatorio_vendas.xlsx')
        return send_file(file_path, as_attachment=True, download_name="relatorio_vendas.xlsx")