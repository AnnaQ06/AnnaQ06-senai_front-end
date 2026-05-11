"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template
    
@bp.route("/dashboard") # cria uma rota
def dashboard(): # função que gerencia rota
    """ Painel de vendas"""
    # if 'user' not in session:
    #     return redirect(url_for("auth.login"))
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    Vendas: list = [
        {"mes":"Janeiro", "total":14951.19},
        {"mes":"Fevereiro", "total":13400.19},
        {"mes":"Março", "total":23200.19},
        {"mes":"Abril", "total":13641.19},
        {"mes":"Maio", "total":12450.19},
        {"mes":"Junho", "total":11951.19},
        {"mes":"Julho", "total":15555.19},
        {"mes":"Agosto", "total":19472.19},
        {"mes":"Setembro", "total":33455.19},
        {"mes":"Outubro", "total":12342.19},
        {"mes":"Novembro", "total":33465.19},
        {"mes":"Dezembro", "total":11236.19},

    ] #Fim lista de vendas

    return render_template("dashboard/index.html", title="Painel de vendas", Vendas=Vendas, locale=locale ) # Renderiza um template
