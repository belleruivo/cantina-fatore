from flask import render_template

def employees_list():
    return render_template("employees.html", show_sidebar=True)