#Criado 23/03/2023

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuario/<nome>")
def usuario(nome):
    return render_template("usuarios.html", nome=nome)


if __name__ == "__main__":
    app.run(debug=True)
