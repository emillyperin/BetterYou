from flask import Flask, render_template, request

app = Flask("Better You")

# Lista de hábitos
habits = ["test1", "test2"]


@app.route("/")
def home():
    return render_template("index.html", habits=habits, title="BetterYou")


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
    return render_template("add_habit.html", title="Better You - Adicionar")


if __name__ == "__main__":
    app.run(debug=True)
