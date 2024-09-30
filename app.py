
from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
db = SQL("sqlite:///dart_scorer.db")

#the_number = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    db.execute("DELETE FROM the_number WHERE id = ?",id)
    return redirect("all_scores")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    all_the_scores = []
    all_the_scores.append(float(request.form.get("score")))
    all_the_scores.append(float(request.form.get("score2")))
    all_the_scores.append(float(request.form.get("score3")))
    all_the_scores.append(float(request.form.get("score4")))
    all_the_scores.append(float(request.form.get("score5")))
    score = str(sum(all_the_scores))
    #the_number [name] = score
    #return render_template("success.html")
    db.execute("INSERT INTO the_number (name,score) VALUES (?,?)",name,score)
    return redirect("/all_scores")

@app.route("/all_scores")
def all_scores():
    all_scores = db.execute("SELECT * FROM the_number")
    return render_template("all_scores.html", all_scores = all_scores)

@app.route("/main_page")
def main_page():
    return render_template("index.html")

@app.route("/score_page")
def score_page():
    return redirect("/all_scores")