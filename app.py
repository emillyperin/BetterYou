######################################## BETTER YOU ########################################

import datetime
import uuid

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    "Better You", template_folder="templates"
)  # *****Revisa isso aqui***** Qnd tu dá open folder no VScode (CTRL+K) tem que escolher o diretório BetterYou ou os templates não serão achados.


# Estabelece um Uniform Resource Identifier para o banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///habits.db"

# Cria um object de banco de dados.
# SQLAlchemy é uma biblioteca de Mapeamento Objeto-Relacional que faz a conversão de dados relacionais para objetos em memória.
db = SQLAlchemy(app)


########################################  MODELS  ########################################


# Estabelece modelo Habits com colunas: id, description, date_created, completions.
class Habits(db.Model):
    # Número de identificação do hábito
    id = db.Column(
        db.String(36),
        primary_key=True,
    )

    # Descrição/nome do hábito
    description = db.Column(db.String(200), nullable=False)

    # Data de criação do hábito (FORMATO DATETIME)
    date_created = db.Column(db.DateTime, default=datetime.date.today())

    # Criando relacionamento 1 pra 1 com Completions (uselist=False)
    completions = db.relationship(
        "Completions", backref="habit", uselist=False, lazy=True
    )

    # Cria uma ID única para cada hábito (REDUNDANTE)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())

    # Representação em uma string do id pra facilitar depuração dos hábitos
    def __repr__(self):
        return "<Habits %r>" % self.id


# Estabelece modelo Completions com as colunas: id, date_completed(não está sendo usado nos templates por hora), habit_uuid.
class Completions(db.Model):
    # Número de identificação do hábito completado
    id = db.Column(db.Integer, primary_key=True)

    # Data em que o hábito foi completado
    date_completed = db.Column(db.DateTime, default=datetime.date.today())

    # Coluna com a ID única do Hábito parente utilizando uma ForeignKey.
    habit_uuid = db.Column(db.String(36), db.ForeignKey("habits.id"))


######################################## DECORADORES ########################################


# Dando acesso (contexto) a todos os templates para a função date_range pra não precisar passá-la individualmente
@app.context_processor
def add_calc_date_range():
    # Cria uma lista dinâmica de datas a partir do dia START (selected_date). A lista vai de X,X dias antes/depois.
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-5, 6)]
        return dates

    return {"date_range": date_range}


# ROTA PARA A PÁGINA INICIAL
@app.route("/", methods=["GET", "POST"])
def index():
    # Request do query param: caso ele não exista, atribui o dia de hj para 'selected_date' e cria a lista de datas a partir daí.
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.datetime.fromisoformat(date_str)
    else:
        selected_date = datetime.datetime.today()

    # Query dos dados do model para 'habit'
    habit = Habits.query.order_by(Habits.date_created)

    # Passando o dados de Completions para completed_habit
    completed_habit = Completions.query.order_by(Completions.date_completed)

    # Renderizando template HMTL e passando as variáveis úteis a ele.
    return render_template(
        "index.html",
        title="Better You",
        habit=habit,
        completed_habit=completed_habit,
        selected_date=selected_date,
    )


# ROTA PARA PÁGINA DE ADICIONAR HÁBITOS
@app.route("/add", methods=["GET", "POST"])
def add_habit():
    # Quando o botão Adicionar for acionado POST requisita string dentro da text area.
    if request.method == "POST":
        new_description = request.form.get("input_description")
        new_habit = Habits(description=new_description)

        # Commit à DB dos dados requisitados
        try:
            db.session.add(new_habit)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            # Printando string no console pra facilitar debug
            print("ERROR:", str(e))
            return "ERRO AO ADICIONAR NOVO HÁBITO: " + str(e)

    else:
        return render_template(
            "add_habit.html",
            title="Better You - Adicionar",
            selected_date=datetime.datetime.today(),
        )


# DEFINE ROTA DO BOTÃO QUE COMPLETA TASKS
@app.route("/complete", methods=["POST"])
def complete():
    # request dos inputs nominados 'habitId' e 'habitDate'
    completed_habit_id = request.form.get("habitId")
    completed_habit_date_str = request.form.get("habitDate")

    # Try/except que converte string em obj datetime usado pra debug *obsoleto deletar depois
    try:
        completed_habit_date = datetime.datetime.fromisoformat(completed_habit_date_str)
    except ValueError:
        return "ERRO AO COMPLETAR HÁBITO: Invalid date format"

    # Fazendo entrada dos dados requisitados
    completed_habit_data = Completions(
        habit_uuid=completed_habit_id, date_completed=completed_habit_date
    )

    # Passando os dados completos pra DB e dando commit.
    try:
        db.session.add(completed_habit_data)
        db.session.commit()
        return redirect("/")

    # Pescando exceptions pra facilitar debug
    except Exception as e:
        print("ERROR:", str(e))
        return "ERRO AO COMPLETAR HÁBITO"


######################################## INICIALIZAÇÃO DO BANCO DE DADOS ########################################

# cria db caso ela não exista. (pra zerar a db basta fechar o app, deletar '../instance/habits.db', e executar o app novamente)
# Necessário baixar a extensão SQLite Viewer no VSCode para vizualizar a database e facilitar o trabalho.
with app.app_context():
    db.create_all()

########################################     INICIALIZAÇÃO DO FLASK     #########################################

if __name__ == "__main__":
    app.run(debug=True)  # True or false pra debug mode.
