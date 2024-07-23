from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    context = {
        'title': 'Главная страница',
        'active_link': 1
    }
    return render_template('index.html', **context)

@app.route("/blog/")
def blog():
    context = {
        'title': 'Блог',
        'active_link': 2
    }
    return render_template('blog.html', **context)

@app.route("/contacts/")
def contacts():
    context = {
        'title': 'Контакты',
        'active_link': 3
    }
    return render_template('contacts.html', **context)

if __name__ == '__main__':
    app.run()
