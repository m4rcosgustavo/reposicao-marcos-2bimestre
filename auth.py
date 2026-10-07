from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


# Rota /registro
@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        usuario_existente = database.buscar_usuario_por_email(email)
        if usuario_existente is not None:
            flash("E-mail já cadastrado.")
            return redirect(url_for("auth.registro"))

        senha_hash = generate_password_hash(senha)
        database.criar_usuario(nome, email, senha_hash)
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for("auth.login"))

    return render_template("registro.html")


# Rota /login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        usuario = database.buscar_usuario_por_email(email)
        if usuario and check_password_hash(usuario["senha"], senha):

    

            return redirect(url_for("auth.login"))

        flash("E-mail ou senha inválidos.")

    return render_template("login.html")


# Rota /logout
@auth_bp.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))
    return redirect(url_for("index"))