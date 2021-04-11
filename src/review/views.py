from . import app
from .forms import SubmitForm

from flask import render_template
from models.review import ReviewModel


@app.route('/')
def index():
    return render_template('welcome.html')


@app.route('/form/', methods=('GET', 'POST'))
def form():
    myform = SubmitForm()

    if myform.is_submitted():
        line = myform.review_text.data
        review_model = ReviewModel()
        sentiment, hilightwords = review_model.predict(line)

        return render_template('result.html',
                               line=line,
                               highlight_words=hilightwords,
                               sentiment=sentiment
                               )

    return render_template('form.html', form=myform)


@app.route('/result/')
def submit():
    return render_template('result.html')


@app.route('/about')
def about():
    return 'This page run segment analysis on review text'


@app.route('/author')
def author():
    return 'ycai'
