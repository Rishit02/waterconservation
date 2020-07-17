from flask import Flask, render_template

app = Flask(__name__)

#navbar to remain at top ==> top: 0;

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html")

@app.route("/pledge")
def pledge():
    return render_template("pledge.html")

@app.route("/congrats", methods=["POST"])
def congrats():
    return render_template("congrats.html")

@app.route("/innovation")
def innovate():
    return render_template("innovate.html")

if __name__=="__main__":
    app.run(debug=True)
