from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def entry():
    return render_template("entry.html")


@app.route("/selection_menu", methods=['GET', 'POST'])
def selection_menu(username):
    return render_template("selection_menu.html", username=username)


@app.route("/question_page", methods=['GET', 'POST'])
def quizzes(username, quizzID, quizz_content):
    # if request.method == "POST":
    #     quizz_answer = request.form.get("quizz_answer")
    #     return
    return render_template("question_page.html", username=username, quizzID=quizzID, quizz_content=quizz_content)


@app.route("/answer_returner", methods=['GET', 'POST'])
def answer_returner(username, quizzID, answer_content):
    if request.method == "POST":
        quizz_answer = request.form.get("quizz_answer")
        if get_answer(
                quizzID) == quizz_answer.lower():  # t.d. need to build the function that extrapolates answer for QuizzID
            # correct_answer(username,
            #                quizzID)  # t.d. need to build a function that mods the userdata on that id as correct
            return render_template("well_done.html", username=username,
                                   quizzID=quizzID)  # t.d. need to create and edit a well_done.html to loop back to selection_menu
        else:
            # false_answer(username,
            #              quizzID)  # t.d. need to build a function that mods the userdata on that id as incorrect
            return render_template("sorry_wrong.html", username=username,
                                   quizzID=quizzID)  # t.d. need to create and edit a sorry_wrong.html to loop back to selection_menu


@app.route("/well_done")
def well_done(username, quizzID):
    return render_template("well_done.html", username=username, quizzID=quizzID)

def sorry_wrong(username, quizzID):
    return render_template("sorry_wrong.html", username=username, quizzID=quizzID)


if __name__ == "__main__":
    app.run(debug=True)
