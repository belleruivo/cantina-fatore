from flask import render_template

def reports():
    return render_template("reports.html", show_sidebar=True)