from flask import render_template

# falta as classes (POO e os 17 conceitos a serem abordados), isso foi so um exemplo com rota configurada
def reports():
    return render_template("reports.html", show_sidebar=True)