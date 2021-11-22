from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
from ArticleFinder import Finder
from transformers import pipeline

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(50), nullable = False)
    passw = db.Column(db.String(50), nullable = False)
    token = db.Column(db.String(120), nullable = False)
    def __repr__(self):
        return self.token

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.Text, nullable=False)
    coin = db.Column(db.Text, nullable=False)
    fulltext = db.Column(db.Text, nullable=True)
    summary = db.Column(db.Text, nullable=True)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/find', methods=['POST'])
def find():
    if request.method == "POST":
        _token = request.form['token']
        correctToken = str(User.query.filter_by(token = _token).first())
        if (correctToken == _token):
            scrapper = Finder()
            summarizer = pipeline('summarization')
            print("POST")
            name = request.form['name']
            articles = scrapper.findArticle(name)
            counter = 0
            res = []
            for key,val in articles.items():
                summ = summarizer(val, max_length=100, min_length=30, do_sample=True)
                article = Article(url=key, coin=name,fulltext="val",summary=summ[0]['summary_text'])
                try:
                    db.session.add(article)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    pass
                res.append(article)
            return render_template('index.html', articles=res, name=name)
        else:
            return '<h1>Hello, Could not verify the token</h1>'


@app.route('/db')
def df():
    data = Article.query.all()
    return render_template('index.html', data=data)

@app.route('/db_delete_all')
def db_detete_all():
    try:
        num_rows_deleted = db.session.query(Article).delete()
        db.session.commit()
    except:
        db.session.rollback()
    return render_template('index.html', data=None, num_rows_deleted=num_rows_deleted)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        _login = request.form['login']
        _passw = request.form['passw']
        correctToken = str(User.query.filter_by(login = _login).first())
        data = _login + _passw
        if correctToken == md5(data.encode('utf-8')).hexdigest():
            return '<b>Token: </b>' + correctToken
        else:
            return 'Could not found a user with login: ' + _login
    else:
        return render_template('login.html')

@app.route('/protected', methods = ['GET'])
def protected():
    if request.method == 'GET':
        _token = request.args.get('token')
        correctToken = str(User.query.filter_by(token = _token).first())
        if (correctToken == _token):
            return '<h1>Hello, token which is provided is correct</h1>'
        else:
            return '<h1>Hello, Could not verify the token</h1>'

if __name__ == '__main__':
    app.run(debug = True) 