from flask import Flask, render_template, request, redirect
from models import Answer, Question, db
from random import shuffle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/work')
def work():
    return render_template('work.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route("/test_1", methods=['GET', 'POST'])
def test_1():
    question = Question.query.filter(Question.dif == "easy").all()
    answer = Answer.query.all()
    shuffle(answer)
    return render_template('test.html', questions=question, answers=answer)


@app.route('/test_2')
def test_2():
    question = Question.query.filter(Question.dif == "medium").all()
    answer = Answer.query.all()
    shuffle(answer)
    return render_template('test.html', questions=question, answers=answer)


@app.route('/test_3')
def test_3():
    question = Question.query.filter(Question.dif == "hard").all()
    answer = Answer.query.all()
    shuffle(answer)
    return render_template('test.html', questions=question, answers=answer)


@app.route("/result", methods=['POST'])
def result():
    reponse = list(map(
        lambda qa: (int(qa[0]), int(qa[1])),
        [k.split(', ') for k in request.form.keys()]
    ))
    print(reponse)
    count = 0
    for q, a in reponse:
        question = Question.query.filter(Question.id == q).first()
        answer = Answer.query.filter(Answer.id == a).first()
        if answer.question_id == question.id and answer.is_true:
            count += 1
    if count < len(reponse):
        return render_template('/fail.html', c=count, size=len(reponse))
    return render_template('/success.html', c=count, size=len(reponse))


if __name__ == '__main__':
    app.run(debug=True)
