from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired
from mod.models import Tarefas
from mod import db

class TarefasForm(FlaskForm):
    data = DateField()
    time = StringField(validators=[DataRequired()], render_kw={"placeholder": "HH:MM"})
    tarefa = StringField('', validators=[DataRequired()])
    btn = SubmitField('Add')

    def save(self):
        nova_tarefa = Tarefas(
            data=self.data.data,
            time=self.time.data,
            tarefa=self.tarefa.data
        )

        db.session.add(nova_tarefa)
        db.session.commit()
        return nova_tarefa