from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def entry():
    return render_template("entry.html")

@app.route("/selection_menu")
def selection_menu(username):
    return render_template("selection_menu.html", username=username)

@app.route("/question_page")
def quizzes(username, quizzID, quizz_content):
    return render_template("quizzes.html", username=username, quizzID=quizzID, quizz_content=quizz_content)

if __name__ == "__main__":
    app.run(debug=True)