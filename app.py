# app.py

import os
from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        nome = request.form['nome']
        cliente = Clientes(cpf, telefone, nome)
        db.session.add(cliente)
        db.session.commit()
    cliente = Clientes.query.all()
    return render_template('index.html', cliente=cliente)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
