from flask import Flask, escape, url_for
app = Flask(__name__)


@app.route('/')
def index():
  return 'Index Page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)