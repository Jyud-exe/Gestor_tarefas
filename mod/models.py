from mod import db

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    data = db.Column(db.Date, default=db.func.current_date())
    time = db.Column(db.String, nullable=True)
    tarefa = db.Column(db.String, nullable=True)

    