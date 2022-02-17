from flask import Flask
from flask.templating import render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/services")
def services():
    return render_template('index.html')


@app.route("/departments")
def departments():
    return render_template('index.html')


@app.route("/doctors")
def doctors():
    return render_template('index.html')


@app.route("/diabetes")
def diabetes():
    return render_template('diabetes.html')


app.run(debug=True)
