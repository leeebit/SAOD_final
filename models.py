from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question_number = db.Column(db.Integer, nullable = False)
    dif = db.Column(db.String(6), nullable = False)
    question = db.Column(db.String(500), nullable = False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    answer = db.Column(db.String(500), nullable = False)
    is_true = db.Column(db.Boolean, nullable = False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable = False)
    question = db.relationship('Question', backref=db.backref('answers', lazy=True))