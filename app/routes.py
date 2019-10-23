from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Zaphod'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'You are very nice MR Beeblebrox '
        },
        {
            'author': {'username': 'Zaphod'},
            'body': "If there's anything more important than my ego around, I want it caught and shot now."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)