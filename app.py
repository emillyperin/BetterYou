import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask("Better You",template_folder="templates")   # *****Revisa isso aqui*****

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///habits.db"

db = SQLAlchemy(app)


# Models
class Habits(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Número de identificação do hábito
    description = db.Column(db.String(200), nullable=False)  # Descrição/nome do hábito
    date_created = db.Column(
        db.DateTime, default=datetime.date.today()
    )  # Data de criação do hábito

    def __repr__(self):
        return "<Name %r>" % self.id


# Não implementado ainda
class Completions(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # Número de identificação do hábito completado
    description = db.Column(
        db.String(200), nullable=False
    )  # Descrição/nome do hábito completado
    date_created = db.Column(
        db.DateTime, default=datetime.date.today()
    )  # Data em que o hábito foi completado (redundante)

    def __repr__(self):
        return "<Name %r>" % self.id


# Dando acesso a todos os templates para a função date_range
@app.context_processor
def add_calc_date_range():
    # Cria uma lista de datas a partir do dia de hoje que vai de 3 dias antes/depois
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}  # context_processor retorna um dict


# Rota para página inicial
@app.route("/", methods=["GET", "POST"])
def index():
    # Request do query param: caso ele não exista, atribui o dia de hj para 'selected_date'
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.datetime.fromisoformat(date_str)
    else:
        selected_date = datetime.datetime.today()

    # Buscando a descrição/nome do hábito na db e atribuindo a uma variável
    habit = Habits.query.order_by(Habits.date_created)

    return render_template(
        "index.html",
        title="Better You",
        habit=habit,
        selected_date=selected_date,
    )


# Cria rota para página de adicionar hábitos
@app.route("/add", methods=["GET", "POST"])
def add_habit():
    # Método POST requisita dados do <form> com nome "input_description" e salva em uma variável, caso não houver POST renderiza a pág normalmente
    if request.method == "POST":
        new_description = request.form.get("input_description")
        new_habit = Habits(description=new_description)

        # Commit à DB dos dados requisitados
        try:
            db.session.add(new_habit)
            db.session.commit()
            return redirect("/")
        except:
            return "ERRO AO ADICIONAR NOVO HÁBITO"

    else:
        return render_template(
            "add_habit.html",
            title="Better You - Adicionar",
            selected_date=datetime.datetime.today(),
        )


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
