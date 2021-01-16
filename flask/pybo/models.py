from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False) # 글자수 제한없음 Text
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set', ))
    # question = db.relationship('Question', \
    #                            backref=db.backref('answer_set', \
    #                                               cascade='all, delete-orphan' ))
    #                             # 이렇게 하면 질문과 연관된 답변 데이터 전부 삭제
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


