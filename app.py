from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SOLALCHEMY TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), primary_key=False)
    intro = db.Column(db.String(300), primary_key=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r' % self.id


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():  # put application's code here
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(titlte=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/home')
        except:
            return  "При добавлении статьи произошла ошибка"
    else:
        return render_template("create-article.html")






if __name__ == '__main__':
    app.run(debug=True)
