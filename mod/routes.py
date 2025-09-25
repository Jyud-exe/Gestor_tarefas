from mod import app
from flask import render_template, redirect, url_for
from mod.forms import TarefasForm
from mod.models import Tarefas
from mod import db

@app.route('/', methods=['GET', 'POST'])
def home():
    lista = Tarefas.query.order_by(Tarefas.time.asc())
    return render_template("index.html", lista=lista)

@app.route('/addtarefa', methods=['GET', 'POST'])
def add_tarefa():
    form = TarefasForm()
    if form.validate and form.is_submitted():
        form.save()
        return redirect(url_for('home'))
    return render_template('add_tarefas.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    tarefa = Tarefas.query.get(id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect(url_for('home'))